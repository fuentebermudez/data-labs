import pandas as pd
import numpy as np
import Extract as e
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestRegressor


def scale(df):
    transformer = RobustScaler().fit(df)
    transformed_data=transformer.transform(df)
    return transformed_data

def remove_columns(data,treshold):
    for column in data.columns:
        n_rows=len(data[column])
        n_nulls=data[column].isna().sum()
        percentage_nulls=(n_nulls/n_rows)*100
        if percentage_nulls>treshold:
            data.drop(labels=column,axis=1,inplace=True)
    return data

def predict_odometer(cars_prices):
    df_odo = cars_prices.dropna()
    X = df_odo[['year']]
    y = df_odo['odometer']
    from sklearn.model_selection import train_test_split

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33, random_state=1)

    from sklearn.linear_model import LinearRegression
    reg_odometer = RandomForestRegressor(max_depth=3, random_state=0, n_estimators=100)
    #reg_odometer = LinearRegression(normalize=True).fit(X_train, Y_train)

    reg_odometer.fit(X, y)
    y_real = reg_odometer.predict(np.array(cars_prices['year'].fillna(method='ffill')).reshape(-1, 1))

    return pd.Series(y_real)

def predict_condition(cars_prices):
    from sklearn import preprocessing
    df_odo = cars_prices.dropna()

    le = preprocessing.LabelEncoder()
    le.fit(df_odo.condition.unique())
    df_odo.condition = le.transform(df_odo.condition)

    # Entrenamos el modelo

    X = df_odo[['year', 'odometer']]
    y = df_odo['condition']

    from sklearn.model_selection import train_test_split

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    from sklearn.linear_model import LinearRegression
    reg_condition = LinearRegression(normalize=True).fit(X_train, Y_train)

    # Labelizamos

    from sklearn import preprocessing
    cars_prices.condition.fillna('desconocido', inplace=True)
    le = preprocessing.LabelEncoder()
    le.fit(cars_prices.condition.unique())
    cars_prices.condition = le.transform(cars_prices.condition)

    # Aplicamos modelo
    condition = pd.Series(reg_condition.predict(X_train))
    cars_prices['condition'].fillna(condition,inplace=True)

    return cars_prices

def process_title_status(cars_prices):
    cars_prices['title_status'].fillna('other',inplace=True)
    cars_prices['title_status'].replace({'clean':'good','rebuilt':'regular','lien':'bad','missing':'bad','parts only':'bad','salvage':'bad'},inplace=True)
    from sklearn import preprocessing

    le = preprocessing.LabelEncoder()
    le.fit(cars_prices['title_status'].unique())
    cars_prices['title_status']=le.transform(cars_prices['title_status'])
    return cars_prices

cars_country = pd.read_csv("..\data\cars_manufacturers.csv")

def add_manufacturer_country(cars_country, cars_prices):
    cars_prices = pd.merge(cars_prices, cars_country, on='manufacturer', how='left')
    cars_prices = pd.get_dummies(cars_prices, prefix=['country'], columns=['country'])
    return cars_prices

def get_n_cylinders(cylinders):
    cylinders=cylinders.replace('other','0 cylinders')
    cylinders.fillna('0 cylinders',inplace=True)
    n_cylinders=[int(x[0]) for x in cylinders.str.split(" ")]
    return n_cylinders

def process_type(cars_prices):
    dict_redcution={'SUV': 'Familiar', 'bus': 'Other', 'convertible':'Deportivo','coupe':'Deportivo','hatchback':'Deportivo','mini-van':'Familiar','offroad':'Todo terreno','other':'other', 'pickup':'Camion','sedan':'Familiar','truck':'Camion','van':'Familiar','wagon':'Familiar'}
    cars_prices.type.replace(dict_redcution,inplace=True)
    cars_prices.type.fillna("other",inplace=True)
    types_dummies=pd.get_dummies(cars_prices.type)
    dummies_df=pd.concat([cars_prices,types_dummies],axis=1)
    return dummies_df

def remove_outliers(cars_prices,column):
    q_25=cars_prices[column].quantile(0.05)
    q_75=cars_prices[column].quantile(0.95)
    cars_prices=cars_prices[(cars_prices[column]>=q_25) & (cars_prices[column]<=q_75)]
    return cars_prices

#Main
def Transform(df):
    df = remove_columns(df, 60)
    #df['odometer'].fillna(predict_odometer(df), inplace=True)
    #df=predict_condition(df)
    df = process_title_status(df)
    df['cylinders'] = get_n_cylinders(df['cylinders'])
    df=add_manufacturer_country(cars_country,df)
    df=process_type(df)
    return df

def get_data():
    train_path="..\data\cars_train.csv"
    submision_path="..\data\cars_test.csv"

    cars_prices=e.load_data(train_path)
    cars_prices_test=e.load_data(submision_path)

    cars_prices=remove_outliers(cars_prices,'price')
    cars_prices=remove_outliers(cars_prices,'odometer')

    cars_prices_t=Transform(cars_prices)
    cars_prices_test_t=Transform(cars_prices_test)

    cars_prices_t.dropna(inplace=True)

    return [cars_prices_t,cars_prices_test_t]