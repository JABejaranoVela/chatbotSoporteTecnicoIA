# Project Plan

## Phase 1. Repository Base
- Define contributor rules and project scope.
- Create the folder structure, dependencies list, README, and FastAPI skeleton.
- Leave the chatbot logic unimplemented.

## Phase 2. Core API and Data
- Add configuration handling and basic API routers.
- Create JSON knowledge files and SQLite initialization utilities.
- Define Pydantic models for requests, responses, and stored interactions.

## Phase 3. Rule-Based Support Layer
- Implement simple technical-support rules in Python.
- Add FAQ lookup and deterministic fallback responses.
- Validate common support scenarios with unit tests.

## Phase 4. NLP Pipeline
- Add spaCy preprocessing for normalization and token handling.
- Add sentence-transformers embeddings and scikit-learn helpers for retrieval or ranking.
- Keep the pipeline modular so rules and NLP can be combined cleanly.

## Phase 5. Frontend
- Build a lightweight HTML + Bootstrap + JavaScript interface.
- Connect the UI to FastAPI endpoints.
- Keep the frontend simple, readable, and academic.

## Phase 6. Validation and Documentation
- Expand tests for endpoints, rules, and NLP behavior.
- Document architecture, dataset assumptions, and limitations.
- Prepare the project for local academic demonstrations.
