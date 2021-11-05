import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from joblib import load
from pdb import set_trace


def eda():
    df = pd.read_parquet("qsa_lgbm_p2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    dummy_reg = DummyRegressor(strategy="mean")
    dummy_reg.fit(X, y)
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)
    yh_dr = dummy_reg.predict(X)
    yh_lr = lin_reg.predict(X)
    mse_dr = mean_squared_error(y, yh_dr)
    mse_lr = mean_squared_error(y, yh_lr)
    set_trace()


def tr_ridge():
    df = pd.read_parquet("sa.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    clf = RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1, 10, 100, 1000]).fit(X, y)
    sc = clf.score(X, y)
    yh_ridge = clf.predict(X)
    mse_ridge = mean_squared_error(y, yh_ridge)
    set_trace()


if __name__ == '__main__':
    eda()
    # tr_ridge()