from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.externals import joblib

#beginning of class
class Model:
#static member
    __classifiers_dict = {
        "K-NN": KNeighborsClassifier(n_neighbors=5),
        "DT": DecisionTreeClassifier(max_depth=3)
    }
#public methods
    def __init__(self, dataset, train_size=0.8, test_size=0.2, classifier=None):
        data = pd.read_csv(dataset, index_col=0).reset_index(drop=True)
        #targetの列をdropする
        self.__train = data.drop("target", axis=1)
        self.__ans = data["target"]
        self.X_train, self.X_test, self.Y_train, self.Y_test = \
        train_test_split(self.__train, self.__ans, train_size=train_size, test_size=test_size, random_state=0)
        self.__model = None
        self.__classifier = classifier

        self.__model = Model.__classifiers_dict[classifier]
        self.__model.fit(self.X_train, self.Y_train)
    
    def predict(self, features):    
        return self.__model.predict(features)
    
    def score(self):
        return self.__model.score(self.X_train, self.Y_train)

    @staticmethod
    def get_classifiers_info() -> dict:
        return Model.__classifiers_dict
#end of class

if __name__ == "__main__":
    model = Model("./dataSet/audioDataSet.csv", 0.8, 0.2, "K-NN")
    joblib.dump(model, "audio_model_KNN.sav")
    
    model_s = joblib.load("./audio_model_KNN.sav")
    result = model_s.predict([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
    print(result)