# Project Plan

## Phase 1. Repository Base
- Define contributor rules and project scope.
- Create the folder structure, dependencies list, README, and FastAPI skeleton.
- Status: completed.

## Phase 2. Core API and Data
- Add configuration handling and basic API routers.
- Create JSON knowledge files for FAQs, intents, rules, and evaluation queries.
- Define Pydantic models for request and response contracts.
- Status: completed without SQLite persistence in the current repository state.

## Phase 3. Rule-Based Support Layer
- Implement simple technical-support rules in Python.
- Add FAQ lookup and deterministic fallback responses.
- Validate common support scenarios with unit tests.
- Status: completed for the current academic prototype.

## Phase 4. NLP Pipeline
- Add spaCy preprocessing for normalization and token handling.
- Add scikit-learn helpers for intent classification.
- Keep the pipeline modular so rules and NLP can be combined cleanly.
- Status: partially completed. The repository includes preprocessing plus TF-IDF and LogisticRegression classification. Embeddings-based retrieval is not implemented yet.

## Phase 5. Frontend
- Build a lightweight HTML + Bootstrap + JavaScript interface.
- Connect the UI to FastAPI endpoints.
- Keep the frontend simple, readable, and academic.
- Status: completed at a minimal level.

## Phase 6. Validation and Documentation
- Expand tests for endpoints, rules, and NLP behavior.
- Document architecture, dataset assumptions, and limitations.
- Prepare the project for local academic demonstrations.
- Status: in progress. Core docs and validation exist, but they should continue evolving with future phases.
