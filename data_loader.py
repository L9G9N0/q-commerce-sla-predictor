import pandas as pd
import logging

def load_and_clean_data(path):
    logging.info("Cleaning data...")
    df = pd.read_csv(path)
    # Tera notebook wala cleaning logic yahan copy-paste kar
    df['Delivery Delay'] = df['Delivery Delay'].map({'Yes': 1, 'No': 0})
    return df