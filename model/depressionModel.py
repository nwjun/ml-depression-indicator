import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class DepressionModel:
    def __init__(self,filename):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_dim=15))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(1, activation="sigmoid"))
        self.model.load_weights(filename)
    
    def predict(self, X):
        result = self.model.predict(np.array(X).reshape(1, -1))[0] >= 0.8
        confidence = self.model.predict(np.array(X).reshape(1, -1))[0]
        return result, confidence
        