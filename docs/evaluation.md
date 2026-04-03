# Evaluation Notes

## Purpose
This document describes the formal evaluation of the current chatbot prototype. The goal is to measure whether the system identifies the expected category and returns a stable response within the current academic scope.

## Evaluation Dataset
The evaluation dataset is stored in `data/json/evaluation_queries.json`. It contains realistic single-turn support queries for these categories:

- `saludo`
- `wifi`
- `internet`
- `password`
- `correo`
- `impresora`
- `vpn`
- `software`
- `fallback`

Each sample includes:
- user query
- expected category

## Evaluation Procedure
The script `scripts/evaluate_system.py` runs the chatbot logic over all evaluation queries and measures:

- total number of evaluated queries
- number of hits
- global accuracy percentage
- hits and accuracy by category
- approximate average response time in milliseconds

The metric is category-level accuracy. A hit is counted when the predicted category matches the expected category.

## Execution
Run:

```bash
.\.venv\Scripts\python scripts\evaluate_system.py
```

The output is plain text so it can be copied directly into the academic report.

## Interpretation
This evaluation is intentionally simple and aligned with the current project phase. It is useful to validate the prototype, compare future iterations, and document the current system performance before adding more advanced NLP components.
