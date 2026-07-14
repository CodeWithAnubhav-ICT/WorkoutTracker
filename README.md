# 🏋️‍♂️ Natural Language Workout Tracker (Day 38)

A data integration pipeline built during the `#100DaysOfCode` Python challenge. This application leverages Natural Language Processing (NLP) to convert unstructured user input (e.g., *"I ran for 30 minutes"*) into structured metrics, instantly syncing them to a cloud database.

This project connects the **Nutritionix API** with the **Sheety API** to create a zero-friction logging experience.

---

## ⚡ Data Pipeline Workflow

```mermaid
graph LR
    A[User Input Text] --> B(Nutritionix API)
    B -->|NLP Parsing| C(Extract Metrics)
    C -->|JSON Payload| D(Sheety API)
    D -->|REST POST| E[(Google Sheets)]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
