import numpy as np
import pandas as pd

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import GridSearchCV

import Transformer as T
import Extract as e
import Submission as s

def train_and_evaluate(clf, X_train, y_train):

    clf.fit(X_train, y_train)

    print("Coefficient of determination on training set:", clf.score(X_train, y_train))

    return clf


cars_prices_t,cars_prices_test_t=T.get_data()

PARAMETROS=['year','odometer','cylinders','Camion','Deportivo','country_united states']
X=T.scale(cars_prices_t[PARAMETROS])
y=cars_prices_t['price']

X_train, X_test, Y_train,Y_test=train_test_split(X,y,test_size=0.33,random_state=1)


#clf=ExtraTreesRegressor(n_estimators=5, max_features=3,random_state=0)
#clf = RandomForestRegressor(max_depth=3, random_state=0,n_estimators=100)
#clf = LinearRegression(normalize=True)

param_grid = {
    'bootstrap': [True],
    'max_depth': [80, 90, 100, 110],
    'max_features': [2, 3,4],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [100, 200, 300, 1000]
}# Create a based model
clf = RandomForestRegressor()# Instantiate the grid search model
clf = GridSearchCV(estimator = clf, param_grid = param_grid,
                          cv = 3, n_jobs = -1, verbose = 2)

clf=train_and_evaluate(clf,X_train, Y_train)

ids = cars_prices_test_t['Id']
s.create_submission(clf,ids,T.scale(cars_prices_test_t[PARAMETROS]))



