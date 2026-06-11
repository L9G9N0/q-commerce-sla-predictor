import logging
from config import DATA_PATH
from data_loader import load_and_clean_data
from model_pipeline import train_and_predict
from rca_engine import RCAEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("--- STARTING FULL-STACK Q-COMMERCE PIPELINE ---")
    
    # 1. Load Data
    df = load_and_clean_data(DATA_PATH)
    
    # 2. Phase A: Predictive Intelligence
    # Yahan hamara model future delays predict karega
    train_and_predict(df)
    
    # 3. Phase B: Diagnostic Intelligence
    # Yahan hamara AI engine root cause batayega
    engine = RCAEngine(df)
    engine.run_analysis()
    
    logging.info("--- PIPELINE COMPLETED SUCCESSFULLY ---")

if __name__ == "__main__":
    main()