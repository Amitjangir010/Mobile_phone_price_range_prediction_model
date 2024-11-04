import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle
import os

def train_model():
    # Get absolute path to data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), 'data', 'mobile_price_range_data.csv')
    
    # Load data
    df = pd.read_csv(data_path)
    
    # Handle outliers
    def remove_outliers(df, col):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]
        return df

    num_cols = ['px_height', 'fc', 'ram', 'sc_w']
    for col in num_cols:
        df = remove_outliers(df, col)

    # Split features and target
    X = df.drop('price_range', axis=1)
    y = df['price_range']

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)

    # Train SVM model
    model = svm.SVC(kernel='linear', C=1)
    model.fit(X_train, y_train)

    # Save model - Using absolute path
    model_path = os.path.join(current_dir, 'model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model() 