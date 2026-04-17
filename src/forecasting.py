from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df[['day','month','year']]
    y = df['sales']

    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def predict_sales(model, df):
    X = df[['day','month','year']]
    df['forecast'] = model.predict(X)
    return df