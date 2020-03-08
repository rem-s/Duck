from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

#beginning of class TrainModel
class TrainModel:
    __classifiers_dict = {None}
#public methods
    def __init__(self, dataset, train_size=0.8, test_size=0.2):
        data = pd.read_csv(dataset, index_col=0).reset_index(drop=True)
        #targetの列をdropする
        self.__train = data.drop("target", axis=1)
        self.__ans = data["target"]
        self.X_train, self.X_test, self.Y_train, self.Y_test = \
        train_test_split(self.__train, self.__ans, train_size=train_size, test_size=test_size, random_state=0)
        self.__model = None
        self.__classifier = None
    """    
    def train_model(self, classifier):
        raise NotImplementedError
    
    def evaluate_model(self):
        return self.model.score(self.X_test, self.Y_test)
    
    def predict(self, features):
        raise NotImplementedError
    """
    @staticmethod
    def get_classifiers_info() -> dict:
        return TrainModel.__classifiers_dict
    
#end of class TrainModel

#beginning of class AudioModel
class AudioModel(TrainModel):
    __classifiers_dict = {
        "K-NN": KNeighborsClassifier(n_neighbors=5),
        "DT": DecisionTreeClassifier(max_depth=3)
    }
#public methods
    def __init__(self, dataset):
        super().__init__(dataset)
    
    def train_model(self, classifier):
        self.__model = AudioModel.__classifiers_dict[classifier]
        self.__classifier = classifier
        self.__model.fit(self.X_train, self.Y_train)
    
    def predict(self, features):    
        return self.__model.predict(features)
    
    def get_this_classifier(self):
        return AudioModel.__classifilers_dict[self.__classifier]
    
    @staticmethod
    def get_classifiers_info() -> dict:
        return AudioModel.__classifiers_dict
#private methods
#end of class AudioModel