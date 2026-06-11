# src/rca_engine.py (Updated)
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class RCAEngine:
    def __init__(self, data):
        self.data = data
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def run_analysis(self):
        print("\n--- Generating AI RCA Report ---")
        
        # 1. Sample the data (Copy from your notebook logic)
        sample_data = self.data['Customer Feedback'].dropna().sample(n=150, random_state=42).tolist()
        combined_text = "\n".join(sample_data)
        
        # 2. Call the API
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a Supply Chain Analyst. Identify Top 3 Causes for delays."},
                {"role": "user", "content": combined_text}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.2,
        )
        
        # 3. Print AND Save the result
        report = chat_completion.choices[0].message.content
        print(report)
        
        # Save to file (Production artifacts!)
        with open("../rca_report.txt", "w") as f:
            f.write(report)
        print("\n--- RCA Report saved to rca_report.txt ---")