# Limitations and Potential

## Potential of the System
The chatbot already demonstrates a complete academic prototype: user interface, API, preprocessing, intent classification, FAQ retrieval, diagnostic rules, and formal evaluation. It is suitable for explaining the end-to-end design of an intelligent support assistant.

## Current Limitations
- limited training data in `intents.json`
- small FAQ base compared with real service desks
- single-turn interaction only
- no persistent context between queries
- no semantic retrieval for paraphrases outside the current examples
- no integration with real support systems or authentication

## Cases Where It Works Well
- common and repetitive support requests
- clearly worded incidents such as WiFi, VPN, password, or printer problems
- controlled academic demonstrations
- explainable prototype scenarios where transparency is more important than coverage

## Cases Where It May Fail
- complex incidents with multiple simultaneous causes
- very domain-specific hardware or software not represented in the JSON files
- ambiguous or underspecified user messages
- long conversations that require memory of previous turns
- real-world enterprise environments with changing infrastructure or policies

## Academic Interpretation
The system should be understood as an explainable baseline, not as a complete production support platform. Its main value lies in demonstrating the combination of rule-based logic, lightweight NLP, and supervised intent classification in a simple and reproducible way.
