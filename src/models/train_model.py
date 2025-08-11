#Use XG Boost first, to add on time series model after

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import root_mean_squared_error, root_mean_squared_error
import pandas as pd

def prepare_features(df):
    df = df.dropna(subset=['MA50', 'MA200', 'RSI', 'ADX'])
    df['Return'] = df['Close'].pct_change().shift(-1)
    df = df.dropna(subset=['Return'])

    features = ['MA50', 'MA200', 'RSI', 'ADX']
    X = df[features]
    y = df['Return']
    return X, y

def train_xgboost(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)
    model = XGBRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, preds, squared=False)
    print(f"Test RMSE: {rmse:.5f}")
    return model, X_test, y_test, preds
