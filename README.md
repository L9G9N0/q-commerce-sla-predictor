Q-Commerce Operational Intelligence & Diagnostic Engine


Project Context
This project started as an experiment to predict SLA breaches in Q-Commerce logistics using machine learning. However, as I dug deeper into the data, I hit a performance ceiling. Statistical models could tell me that a delay would happen, but they couldn't explain why.

This project evolved from a simple predictive model into a two-tier operational intelligence engine:

Predictive Layer: Uses XGBoost to forecast SLA breaches.

Diagnostic Layer: Uses Large Language Models (LLM) to perform automated Root Cause Analysis (RCA) on unstructured customer feedback.

The Engineering Journey
This wasn't just about training a model; it was about making data actionable.

The Predictive Challenge: After processing the initial dataset, the model accuracy plateaued. The raw data lacked the contextual features required to capture the nuances of "why" a delivery failed (e.g., traffic conditions, picker errors).

The Pivot: Instead of obsessing over incremental gains in model accuracy, I pivoted to a diagnostic approach. I realized that if the model couldn't predict the delay, the customer feedback certainly contained the answers.

The Integration: I integrated the Groq API (Llama-3) to bridge the gap. By sampling customer feedback and piping it through a custom-built prompt, the system now autonomously identifies top-3 logistical failure points, effectively automating the role of a junior supply chain analyst.

System Architecture
I moved away from Jupyter Notebooks to a production-ready, modular architecture. This separation of concerns allows for easier debugging and independent scaling of components.

Plaintext
├── data/               # Raw and processed datasets
├── notebooks/          # EDA and initial experiments
├── src/                # Core production code
│   ├── config.py       # Centralized configuration
│   ├── data_loader.py  # Cleaning and Binarization logic
│   ├── main.py         # Orchestrator (entry point)
│   ├── model_pipeline.py# ML predictive workflow
│   └── rca_engine.py   # GenAI diagnostic engine
├── .env                # API keys (ignored by git)
└── .gitignore          # Strict security rules
How I Tackled Key Challenges
Modularization: Instead of dumping code into one script, I used an Object-Oriented approach. This allows me to test the RCAEngine independently of the ModelPipeline.

API Security: Faced issues with secret management. I implemented strict .gitignore rules to ensure that API keys are never hardcoded or pushed to version control, prioritizing environment security.

Data Quality: Handled complex data cleaning (e.g., mapping non-binary outcomes to binary for classification) within data_loader.py to keep the training loop clean.

LLM Context Windows: To optimize token usage, I implemented a sampling strategy in the RCA engine, ensuring that only relevant, high-impact feedback is sent to the LLM.

Tech Stack
Core: Python 3.10+

ML/Statistics: Scikit-Learn, XGBoost, Pandas

GenAI: Llama-3-70b (via Groq API)

MLOps: Modular architecture, Standard Logging, Environment variables

Getting Started
Prerequisites
Python 3.x

Groq API Key (Sign up at Groq Console)

Installation
Clone the repo:

Bash
git clone https://github.com/L9G9N0/q-commerce-sla-predictor
cd q-commerce-sla-predictor
2. Create your environment file:
   ```bash
   touch .env
   echo "GROQ_API_KEY=your_key_here" >> .env
Install dependencies:

Bash
pip install -r requirements.txt
4. Run the full pipeline:
   ```bash
python src/main.py
Lessons Learned
This project taught me that data engineering is 80% of the battle. Building a model is easy, but building a pipeline that handles real-world, noisy, and unstructured data—and provides a reason for the predictions—is where the real engineering value lies.

Developed by: Hariom
Last Updated: June 2026
