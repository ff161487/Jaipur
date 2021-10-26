import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from joblib import dump
from pdb import set_trace


def LinRegPoly():
    df = pd.read_parquet("qsa.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    model = Pipeline([('poly', PolynomialFeatures(degree=2)),
                      ('linear', LinearRegression(fit_intercept=False))])
    model.fit(X, y)
    dump(model, "lr_p2.joblib")


def lrp2_compare():
    df = pd.read_parquet("qsa_lrp2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    mdl_f = Pipeline([('poly', PolynomialFeatures(degree=2)),
                      ('linear', LinearRegression(fit_intercept=False))])
    mdl_i = Pipeline([('poly', PolynomialFeatures(degree=2, interaction_only=True)),
                      ('linear', LinearRegression(fit_intercept=False))])
    mdl_f.fit(X, y)
    mdl_i.fit(X, y)
    yh_f, yh_i = mdl_f.predict(X), mdl_i.predict(X)
    mse_f, mse_i = mean_squared_error(y, yh_f), mean_squared_error(y, yh_i)
    set_trace()


if __name__ == '__main__':
    lrp2_compare()