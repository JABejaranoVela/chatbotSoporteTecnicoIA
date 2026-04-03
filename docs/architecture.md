# Architecture Notes

## Current State
The project is an academic technical-support chatbot with a simple modular architecture. It already includes:

- FastAPI backend with `/health` and `POST /chat`
- Minimal HTML + Bootstrap + JavaScript interface
- JSON knowledge base with FAQs, intents, rules, and evaluation queries
- spaCy-based preprocessing
- Intent classification with `TfidfVectorizer` + `LogisticRegression`
- FAQ retrieval by category
- Rule-based diagnostic guidance
- Controlled fallback responses
- Automated tests and a formal evaluation script

## Architecture Layers

### 1. Presentation Layer
- Files: `frontend/templates/`, `frontend/static/`
- Responsibility: render the page, send the user query, and display the chatbot response

### 2. API Layer
- Files: `app/main.py`, `app/api/`
- Responsibility: expose HTTP endpoints, validate schemas, and connect frontend with backend logic

### 3. NLP and Classification Layer
- Files: `app/nlp/preprocessing.py`, `app/nlp/intent_classifier.py`
- Responsibility:
  - normalize, tokenize, and lemmatize the message with spaCy
  - classify the intent category with scikit-learn

### 4. Chat Logic Layer
- File: `app/services/chat_service.py`
- Responsibility:
  - receive the normalized text
  - use the predicted category
  - search FAQs for that category
  - fall back to rule-based guidance
  - return a controlled fallback if no useful answer is found

### 5. Data Layer
- Files: `data/json/faqs.json`, `data/json/intents.json`, `data/json/rules.json`, `data/json/evaluation_queries.json`
- Responsibility: store the project knowledge base and evaluation samples in a transparent, editable format

## Current Execution Flow
1. The user submits a message from the web interface.
2. The frontend sends `POST /chat` with `{ "message": "..." }`.
3. FastAPI validates the request with Pydantic.
4. The service preprocesses the text with spaCy.
5. The intent classifier predicts a category from the preprocessed message.
6. The chatbot searches FAQs for that category.
7. If no FAQ is enough, it checks the diagnostic rules for the same category.
8. If no valid answer is found, it returns a controlled fallback.
9. The frontend shows the answer.

## Academic Design Criteria
- Simple and explainable architecture
- No external database in the current phase
- No multi-turn conversation management
- No semantic retrieval yet
- All decisions are inspectable through JSON files and Python modules
