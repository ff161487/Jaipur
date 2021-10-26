import pandas as pd
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


if __name__ == '__main__':
    LinRegPoly()