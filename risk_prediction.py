import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict_risk(temp, humidity, gas):
    data = np.array([[temp, humidity, gas]])
    risk = model.predict_proba(data)[0][1]
    return risk

if __name__ == "__main__":
    risk = predict_risk(45, 60, 780)
    print("Risk Level:", risk)
