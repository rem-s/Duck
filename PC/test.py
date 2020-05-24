import pandas as pd

test_df = pd.read_csv("./audioDataSet.csv", index_col=0).reset_index(drop=True)
test_df.head()

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#targetの列をdropする
X = test_df.drop("target", axis=1)
y = test_df["target"]

#ここから学習用データとテスト用のデータに分ける。random_stateは乱数を固定する
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# k-NN instance, in this time we choose 5-neighbors
model = KNeighborsClassifier(n_neighbors=5)
# construct a model...takes train_data and train_label
model.fit(X_train, y_train)

#### accuracy 97 percent!! ###
print("train score:", model.score(X_train, y_train))
print("test score:", model.score(X_test, y_test))

from sklearn.externals import joblib

joblib.dump(model, 'audio_model_KNN.sav')

# decision tree
from sklearn.tree import DecisionTreeClassifier

# make a instance of decision tree (max_depth = 3)
model = DecisionTreeClassifier(max_depth=3)
# construct a model...train_data and train_label
model.fit(X_train, y_train)

# .scoreで正解率を算出
print("train score:", model.score(X_train, y_train))
print("test score:", model.score(X_test, y_test))

joblib.dump(model, 'audio_model_DT.sav')