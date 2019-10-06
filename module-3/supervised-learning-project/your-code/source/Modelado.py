import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import Transformer as T
import Extract as e

def train_and_evaluate(clf, X_train, y_train):
    clf.fit(X_train, y_train)

    print("Coefficient of determination on training set:", clf.score(X_train, y_train))

    return clf

train_path="..\data\cars_train.csv"
submision_path="..\data\cars_test.csv"

cars_prices=e.load_data(train_path)
cars_prices_test=e.load_data(submision_path)

cars_prices_t=T.Transform(cars_prices)
cars_prices_test_t=T.Transform(cars_prices_test)

cars_prices_t.dropna(inplace=True)
PARAMETROS=['year','odometer','condition','cylinders','SUV',
       'bus', 'convertible', 'coupe', 'hatchback', 'mini-van', 'offroad',
       'other', 'pickup', 'sedan', 'truck', 'van', 'wagon']
X=cars_prices_t[PARAMETROS]
y=cars_prices_t['price']

X_train, X_test, Y_train,Y_test=train_test_split(X,y,test_size=0.33,random_state=1)

clf = LinearRegression(normalize=True)

clf=train_and_evaluate(clf,X_train, Y_train)

ids=cars_prices_test['Id']
X_submission=cars_prices_test_t[PARAMETROS]

X_submission.fillna(method='ffill',inplace=True)

predict=pd.Series(reg.predict(X_submission))

submision=pd.concat([ids, predict], axis=1)
submision.columns=['id','price']

submision.to_csv(path_or_buf='../output/submision.csv',header=True,index=False)





