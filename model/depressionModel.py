import pickle
import numpy as np

class DepressionModel:
    def __init__(self,filename):
        self.model = pickle.load(open(filename, 'rb'))
    
    def predict(self, X):
        return True if self.model.predict(np.array(X).reshape(1, -1))[0] == 1 else False