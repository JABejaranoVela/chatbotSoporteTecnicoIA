from dataclasses import dataclass
from functools import lru_cache
import unicodedata

import spacy
from spacy.language import Language
from spacy.tokens import Doc


@dataclass(frozen=True)
class PreprocessedText:
    normalized_text: str
    tokens: list[str]
    lemmas: list[str]


DOMAIN_LEMMAS = {
    "abre": "abrir",
    "abrelo": "abrir",
    "bloqueada": "bloquear",
    "bloqueado": "bloquear",
    "bloquea": "bloquear",
    "conecta": "conectar",
    "conectaos": "conectar",
    "conectado": "conectar",
    "conectada": "conectar",
    "correo": "correo",
    "correos": "correo",
    "error": "error",
    "funciona": "funcionar",
    "funcionando": "funcionar",
    "impresora": "impresora",
    "imprime": "imprimir",
    "imprimiendo": "imprimir",
    "internet": "internet",
    "login": "login",
    "olvide": "olvidar",
    "olvidado": "olvidar",
    "olvidada": "olvidar",
    "programa": "programa",
    "programas": "programa",
    "sesion": "sesion",
    "software": "software",
    "wifi": "wifi",
}


@Language.component("basic_domain_lemmatizer")
def basic_domain_lemmatizer(doc: Doc) -> Doc:
    for token in doc:
        lemma = DOMAIN_LEMMAS.get(token.text.lower(), token.text.lower())
        token.lemma = doc.vocab.strings.add(lemma)
    return doc


@lru_cache(maxsize=1)
def get_nlp() -> Language:
    nlp = spacy.blank("es")
    nlp.add_pipe("basic_domain_lemmatizer")
    return nlp


def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def preprocess_text(text: str) -> PreprocessedText:
    doc = get_nlp()(text.strip().lower())

    tokens: list[str] = []
    lemmas: list[str] = []

    for token in doc:
        if token.is_space or token.is_punct:
            continue

        token_text = _strip_accents(token.text.lower()).strip()
        lemma_text = _strip_accents((token.lemma_ or token.text).lower()).strip()

        if not token_text:
            continue

        tokens.append(token_text)
        lemmas.append(lemma_text)

    normalized_text = " ".join(lemmas)
    return PreprocessedText(
        normalized_text=normalized_text,
        tokens=tokens,
        lemmas=lemmas,
    )
