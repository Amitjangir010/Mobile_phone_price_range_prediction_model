import pickle
import pandas as pd
import numpy as np

def predict_price_range(features):
    # Load model
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Convert features to DataFrame
    features_df = pd.DataFrame([features])
    
    # Make prediction
    prediction = model.predict(features_df)[0]
    
    return prediction 