# chatbot-soporte-tecnico-ia

Base academica de un chatbot de soporte tecnico en Python. El proyecto ya incluye una API minima, una interfaz web sencilla, FAQs en JSON, diagnostico basico por reglas, preprocesado con spaCy y una clasificacion inicial de intenciones con scikit-learn.

## Stack
- Python
- FastAPI
- Uvicorn
- Pydantic
- spaCy
- scikit-learn
- Reglas en Python
- JSON
- HTML + Bootstrap + JavaScript

## Estructura actual
- `app/`: backend y organizacion principal
- `app/api/`: rutas y endpoints FastAPI
- `app/models/`: esquemas Pydantic
- `app/services/`: logica principal del chatbot
- `app/nlp/`: preprocesado y clasificacion de intenciones
- `data/json/`: FAQs, intenciones, reglas y consultas de evaluacion
- `frontend/templates/`: vistas HTML
- `frontend/static/`: CSS y JavaScript
- `scripts/`: scripts auxiliares, incluida la evaluacion
- `tests/`: pruebas
- `docs/`: documentacion academica

## Puesta en marcha
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API base quedara disponible en `http://127.0.0.1:8000` y la documentacion automatica en `/docs`.

## Alcance de esta fase
- Documentacion persistente del repositorio
- Plan por fases
- API con endpoints `/health`, `/chat` y pagina principal `/`
- Preprocesado basico con spaCy
- Clasificacion de intenciones con TF-IDF + LogisticRegression
- FAQs, intenciones y reglas en JSON
- Script de evaluacion con consultas etiquetadas
- Pruebas basicas de API y clasificacion

## Alcance fuera de esta fase
- Persistencia con SQLite
- Recuperacion semantica con embeddings
- Multi-turno real

## Clasificador de intenciones
- El entrenamiento se hace en memoria al primer uso desde `data/json/intents.json`.
- Cada ejemplo y palabra clave se preprocesa con spaCy antes de alimentar `TfidfVectorizer`.
- El modelo usa `LogisticRegression` y devuelve una categoria con confianza.
- Si la confianza es baja, el sistema cae en `fallback`.

## Evaluacion formal
- El conjunto de evaluacion base esta en `data/json/evaluation_queries.json`.
- El script `scripts/evaluate_system.py` calcula total de consultas, aciertos, porcentaje global, aciertos por categoria y tiempo medio de respuesta.
- Ejecutar:

```bash
.\.venv\Scripts\python scripts\evaluate_system.py
```
