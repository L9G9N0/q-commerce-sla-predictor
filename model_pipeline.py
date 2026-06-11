import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import logging

def train_and_predict(df):
    logging.info("Training Predictive Model (XGBoost)...")
    
    # 1. Prepare Features & Target
    y = df['Delivery Delay']
    leaky_cols = ['Delivery Delay', 'Delivery Time (Minutes)', 'Service Rating', 
                  'Refund Requested', 'Order ID', 'Customer ID', 'Customer Feedback']
    
    # Filter leaky cols from available columns
    features = [c for c in df.columns if c not in leaky_cols]
    X = df[features]
    
    # 2. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    
    # 3. Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. Train Model
    model = XGBClassifier(scale_pos_weight=6.31, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # 5. Evaluate
    y_pred = model.predict(X_test_scaled)
    logging.info("Model Training Complete. Evaluation Report:")
    print(classification_report(y_test, y_pred))
    
    return model