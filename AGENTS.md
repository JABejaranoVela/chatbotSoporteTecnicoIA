# Repository Guidelines

## Scope and Principles
This repository hosts an academic, modular, and intentionally simple technical-support chatbot in Python. Keep the stack fixed to FastAPI, Uvicorn, Pydantic, spaCy, scikit-learn, Python rules, JSON, and a lightweight HTML + Bootstrap + JavaScript frontend. SQLite and sentence-transformers should only be introduced if the project requirements explicitly move into those phases.

Avoid overengineering. Do not introduce React, Angular, Docker, Redis, external databases, message brokers, or cloud-only services unless the project requirements change explicitly.

## Project Structure
Use the repository layout below as the default convention:

- `app/` backend code
- `app/api/` FastAPI routers
- `app/models/` Pydantic schemas
- `app/services/` orchestration services
- `app/nlp/` NLP preprocessing and classification helpers
- `data/json/` curated intents, FAQs, rules, and evaluation samples
- `frontend/templates/` HTML views
- `frontend/static/` Bootstrap assets, custom CSS, and JavaScript
- `scripts/` local evaluation or support scripts
- `tests/` unit and integration tests
- `docs/` academic notes and supporting documentation

## Coding Conventions
Use Python 3.11+ style with 4-space indentation and explicit type hints in public functions. Prefer `snake_case` for files, functions, and variables, `PascalCase` for classes, and descriptive module names such as `intent_classifier.py` or `knowledge_loader.py`.

Keep modules small. Put request and response schemas in `app/models/`, HTTP concerns in `app/api/`, and reusable business logic outside the routers.

## Implementation Rules
Build incrementally. The first implementation target is a clean skeleton, not a full chatbot. Add functionality in phases:

1. Base FastAPI app and project wiring
2. JSON knowledge base and API contracts
3. Rule-based response layer
4. NLP pipeline with spaCy and scikit-learn
5. Evaluation, validation, and documentation

Prefer deterministic, inspectable code over hidden complexity. If a simple ruleset solves a case, do not replace it with a heavier abstraction.

## Testing and Validation
Use `pytest` for tests. Name test files `test_*.py` and mirror the source structure when practical. Test new rules, endpoint contracts, validation behavior, and data-loading code before adding broader NLP features.

## Collaboration Notes
Write focused commits in imperative mood, for example `Add health endpoint skeleton`. Keep README and PLANS aligned with the actual repository state. When adding dependencies, justify them against the approved stack and keep setup friction low for academic use.
