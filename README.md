# chatbot-soporte-tecnico-ia

Base inicial de un chatbot de soporte tecnico con enfoque academico. En esta fase solo se prepara la estructura del proyecto, la documentacion y un esqueleto minimo de FastAPI; la logica completa del chatbot todavia no esta implementada.

## Stack
- Python
- FastAPI
- Uvicorn
- Pydantic
- spaCy
- sentence-transformers
- scikit-learn
- Reglas en Python
- JSON
- SQLite
- HTML + Bootstrap + JavaScript

## Estructura base
- `app/`: backend y organizacion principal
- `data/json/`: archivos de conocimiento e intenciones
- `data/sqlite/`: base SQLite local
- `frontend/templates/`: vistas HTML
- `frontend/static/`: CSS y JavaScript
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
- Estructura base de carpetas
- Dependencias iniciales
- Esqueleto de FastAPI con endpoint de salud
- Skills reutilizables para futuras iteraciones

## Alcance fuera de esta fase
- Clasificacion de consultas
- Recuperacion semantica
- Reglas completas de soporte tecnico
- Persistencia funcional de conversaciones
- Interfaz web completa
