from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
import pandas as pd
#import sys
#from os import listdir, chdir

#beginning of class
class Model(object):
#static member
    __model_dict = {
        "K_NN": "audio_model_KNN.sav",
        "DecisionTree": "audio_model_DT.sav"
    }
#public methods
    def __init__(self):
        self.__model = None
        
    def model_select(self, model):
        self.__model = joblib.load("./control/models/"+Model.__model_dict[model])

    def predict(self, features):
        return self.__model.predict(features)
    
    @staticmethod
    def get_model_info() -> dict:
        return Model.__model_dict
#end of class

if __name__ == "__main__":
    model = Model()
    model.model_select("DecisionTree")