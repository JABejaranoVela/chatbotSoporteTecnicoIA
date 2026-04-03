# fastapi-endpoints

## Purpose
Use this skill to add or update FastAPI endpoints in a modular way without mixing HTTP logic with chatbot rules or NLP code.

## Instructions
- Place routers in `app/api/endpoints/`.
- Keep request and response schemas in `app/models/`.
- Keep endpoint functions thin and move reusable logic into `app/services/`.
- Start with deterministic endpoints such as health, status, or validation.

## Expected Output
- Minimal endpoint files
- Clear route registration in `app/api/routes.py`
