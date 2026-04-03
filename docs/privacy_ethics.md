# Privacy and Ethics

## Privacy of Data
This project is designed for academic use and should not process real personal data. The current knowledge base and evaluation queries use generic, synthetic examples without identifying information.

## No Real Personal Data
The repository does not require names, personal identifiers, private emails, real passwords, or sensitive operational records. Any demonstration should use invented examples only.

## Transparency of the System
The chatbot is not presented as a human operator. Its logic is based on predefined data, spaCy preprocessing, a basic scikit-learn intent classifier, and rule-based responses. This should be explained clearly to users and evaluators.

## Limits of the Chatbot
The system provides first-level technical guidance only. It does not replace a human technician, does not perform real diagnosis on infrastructure, and may fail on ambiguous or very specific incidents.

## Basic Security Measures
- avoid storing real user credentials or support tickets in the repository
- keep the project local in academic demonstrations
- review JSON data before publishing or sharing results
- do not expose the application publicly without additional protections

## Privacy by Design
The current architecture follows a simple privacy-by-design approach:

- minimal data use
- local processing
- no external services required for core behavior
- no persistent storage of conversations in the current phase
- explicit limitation of the chatbot scope and outputs
