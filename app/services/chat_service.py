import json
import re
from pathlib import Path
from typing import Any

from app.models.chat import ChatResponse


FAQS_PATH = Path(__file__).resolve().parents[2] / "data" / "json" / "faqs.json"
INTENTS_PATH = Path(__file__).resolve().parents[2] / "data" / "json" / "intents.json"
RULES_PATH = Path(__file__).resolve().parents[2] / "data" / "json" / "rules.json"
FALLBACK_ANSWER = (
    "No encontre una respuesta clara para esa consulta. "
    "Prueba a reformularla con mas detalle tecnico."
)


def normalize_text(text: str) -> str:
    normalized = text.strip().lower()
    normalized = re.sub(r"[^\w\s]", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def load_faqs() -> list[dict[str, Any]]:
    with FAQS_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("faqs", [])


def load_intents() -> list[dict[str, Any]]:
    with INTENTS_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("intents", [])


def load_rules() -> dict[str, Any]:
    with RULES_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def detect_category(normalized_message: str) -> str:
    for intent in load_intents():
        category = intent.get("category", "fallback")
        examples = {normalize_text(example) for example in intent.get("examples", [])}
        keywords = {normalize_text(keyword) for keyword in intent.get("keywords", [])}

        if any(example in normalized_message for example in examples if example):
            return category

        if any(keyword in normalized_message for keyword in keywords if keyword):
            return category

    return "fallback"


def find_faq_by_category(category: str, normalized_message: str) -> ChatResponse | None:
    message_words = set(normalized_message.split())

    for faq in load_faqs():
        if faq.get("category") != category:
            continue

        keywords = {normalize_text(keyword) for keyword in faq.get("keywords", [])}
        question = normalize_text(faq.get("question", ""))

        if keywords and any(keyword in normalized_message for keyword in keywords):
            return ChatResponse(
                answer=faq["answer"],
                category=category,
                matched=True,
                normalized_message=normalized_message,
                source="faq",
            )

        if question and all(word in message_words for word in question.split()):
            return ChatResponse(
                answer=faq["answer"],
                category=category,
                matched=True,
                normalized_message=normalized_message,
                source="faq",
            )

    return None


def find_rule_by_category(category: str, normalized_message: str) -> ChatResponse | None:
    rules = load_rules().get("rules", {})
    rule = rules.get(category)
    if not rule:
        return None

    answer = rule.get("diagnostic", "").strip()
    if not answer:
        return None

    return ChatResponse(
        answer=answer,
        category=category,
        matched=True,
        normalized_message=normalized_message,
        source="rule",
    )


def find_faq_answer(message: str) -> ChatResponse:
    normalized_message = normalize_text(message)
    category = detect_category(normalized_message)

    faq_response = find_faq_by_category(category, normalized_message)
    if faq_response is not None:
        return faq_response

    rule_response = find_rule_by_category(category, normalized_message)
    if rule_response is not None:
        return rule_response

    return ChatResponse(
        answer=FALLBACK_ANSWER,
        category="fallback",
        matched=False,
        normalized_message=normalized_message,
        source="fallback",
    )
