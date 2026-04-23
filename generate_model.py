import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import random
import pickle
import os

commodity_dict = {
    "arhar": "static/Arhar.csv", "bajra": "static/Bajra.csv", "barley": "static/Barley.csv",
    "copra": "static/Copra.csv", "cotton": "static/Cotton.csv", "sesamum": "static/Sesamum.csv",
    "gram": "static/Gram.csv", "groundnut": "static/Groundnut.csv", "jowar": "static/Jowar.csv",
    "maize": "static/Maize.csv", "masoor": "static/Masoor.csv", "moong": "static/Moong.csv",
    "niger": "static/Niger.csv", "paddy": "static/Paddy.csv", "ragi": "static/Ragi.csv",
    "rape": "static/Rape.csv", "jute": "static/Jute.csv", "safflower": "static/Safflower.csv",
    "soyabean": "static/Soyabean.csv", "sugarcane": "static/Sugarcane.csv",
    "sunflower": "static/Sunflower.csv", "urad": "static/Urad.csv", "wheat": "static/Wheat.csv"
}

trained_models = {}

def train():
    print("Training models...")
    for crop, path in commodity_dict.items():
        if not os.path.exists(path):
            print(f"Warning: {path} not found.")
            continue
        print(f"Processing {crop}...")
        dataset = pd.read_csv(path)
        X = dataset.iloc[:, :-1].values
        Y = dataset.iloc[:, 3].values
        
        depth = random.randrange(7, 18)
        regressor = DecisionTreeRegressor(max_depth=depth)
        regressor.fit(X, Y)
        
        accuracy = regressor.score(X, Y)
        print(f"Accuracy (R^2 Score) for {crop}: {accuracy:.4f}")
        
        trained_models[crop] = {
            'regressor': regressor,
            'X': X,
            'Y': Y,
            'accuracy': accuracy
        }

    with open("model.pkl", "wb") as f:
        pickle.dump(trained_models, f)
    print("Done! model.pkl generated.")

if __name__ == "__main__":
    train()
