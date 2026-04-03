from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_chat_endpoint_returns_wifi_answer() -> None:
    response = client.post("/chat", json={"message": "Mi wifi no conecta"})

    assert response.status_code == 200
    assert response.json()["matched"] is True
    assert response.json()["category"] == "wifi"
    assert response.json()["source"] == "faq"


def test_chat_endpoint_returns_password_answer() -> None:
    response = client.post("/chat", json={"message": "No recuerdo mi contrasena y no puedo iniciar sesion"})

    assert response.status_code == 200
    assert response.json()["matched"] is True
    assert response.json()["category"] == "password"
    assert response.json()["source"] == "faq"


def test_chat_endpoint_returns_impresora_answer() -> None:
    response = client.post("/chat", json={"message": "La impresora no imprime"})

    assert response.status_code == 200
    assert response.json()["matched"] is True
    assert response.json()["category"] == "impresora"
    assert response.json()["source"] == "faq"


def test_chat_endpoint_returns_software_answer() -> None:
    response = client.post("/chat", json={"message": "Un programa da error y no abre"})

    assert response.status_code == 200
    assert response.json()["matched"] is True
    assert response.json()["category"] == "software"
    assert response.json()["source"] == "faq"


def test_chat_endpoint_returns_fallback_when_no_match() -> None:
    response = client.post("/chat", json={"message": "Necesito ayuda con un dispositivo biometrico de laboratorio"})

    assert response.status_code == 200
    assert response.json()["matched"] is False
    assert response.json()["category"] == "fallback"
    assert response.json()["source"] == "fallback"


def test_chat_endpoint_normalizes_message() -> None:
    response = client.post("/chat", json={"message": "   LOGIN!!   "})

    assert response.status_code == 200
    assert response.json()["normalized_message"] == "login"
