import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from app.nlp.preprocessing import preprocess_text


INTENTS_PATH = Path(__file__).resolve().parents[2] / "data" / "json" / "intents.json"
FALLBACK_CATEGORY = "fallback"
CONFIDENCE_THRESHOLD = 0.45


@dataclass(frozen=True)
class IntentPrediction:
    category: str
    confidence: float


def load_intents() -> list[dict[str, object]]:
    with INTENTS_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("intents", [])


def build_training_data() -> tuple[list[str], list[str]]:
    texts: list[str] = []
    labels: list[str] = []

    for intent in load_intents():
        category = str(intent.get("category", FALLBACK_CATEGORY))
        if category == FALLBACK_CATEGORY:
            continue

        samples = list(intent.get("examples", [])) + list(intent.get("keywords", []))
        for sample in samples:
            normalized = preprocess_text(str(sample)).normalized_text
            if not normalized:
                continue

            texts.append(normalized)
            labels.append(category)

    return texts, labels


@lru_cache(maxsize=1)
def get_intent_classifier() -> Pipeline:
    texts, labels = build_training_data()

    classifier = Pipeline(
        steps=[
            ("vectorizer", TfidfVectorizer(ngram_range=(1, 2))),
            ("model", LogisticRegression(max_iter=1000, C=4.0)),
        ]
    )
    classifier.fit(texts, labels)
    return classifier


def classify_intent(message: str) -> IntentPrediction:
    normalized = preprocess_text(message).normalized_text
    if not normalized:
        return IntentPrediction(category=FALLBACK_CATEGORY, confidence=0.0)

    classifier = get_intent_classifier()
    probabilities = classifier.predict_proba([normalized])[0]
    classes = classifier.named_steps["model"].classes_

    best_index = max(range(len(probabilities)), key=probabilities.__getitem__)
    best_category = str(classes[best_index])
    best_confidence = float(probabilities[best_index])

    if best_confidence < CONFIDENCE_THRESHOLD:
        return IntentPrediction(category=FALLBACK_CATEGORY, confidence=best_confidence)

    return IntentPrediction(category=best_category, confidence=best_confidence)
