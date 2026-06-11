# Q-Commerce Logistics Intelligence Engine

## Overview
A modular ML pipeline for Q-Commerce operations. This project addresses two operational requirements: predicting delivery delays (SLA breaches) and performing root cause analysis (RCA) on unstructured customer feedback.

## Engineering Pivot
During development, initial predictive models (XGBoost/LogReg) hit a performance ceiling due to lack of spatial/operational features in the raw dataset. To compensate, I pivoted the architecture to include a diagnostic GenAI pipeline that processes customer feedback to extract operational insights.

## Project Structure
The codebase is modularized for production scalability:
- `src/main.py`: Pipeline orchestrator.
- `src/config.py`: Centralized configuration.
- `src/data_loader.py`: Automated cleaning and Binarization.
- `src/model_pipeline.py`: Predictive ML workflow (Scaling, XGBoost).
- `src/rca_engine.py`: GenAI diagnostic pipeline (Llama-3 via Groq API).

## Technical Stack
- **Languages:** Python
- **ML/Stats:** Scikit-Learn, XGBoost, Pandas, NLTK
- **GenAI:** Groq API (Llama-3.3-70b), Dotenv for security
- **MLOps:** Modular architecture, standard Python logging

## Setup Instructions
1. Clone the repository.
2. Create a `.env` file in the root directory:
   ```text
   GROQ_API_KEY=your_actual_key_here
