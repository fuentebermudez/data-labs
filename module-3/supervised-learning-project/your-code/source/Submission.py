import pandas as pd

def create_submission(clf,ids,cars_prices_test,path_output='../output/submision.csv'):

    X_submission = cars_prices_test

    X_submission.fillna(method='ffill', inplace=True)

    predict = pd.Series(clf.predict(X_submission))

    submision = pd.concat([ids, predict], axis=1)
    submision.columns = ['id', 'price']

    submision.to_csv(path_or_buf=path_output, header=True, index=False)