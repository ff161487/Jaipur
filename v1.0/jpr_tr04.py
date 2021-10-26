import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import RidgeCV
from pdb import set_trace


def eda():
    df = pd.read_parquet("qsa_lrp2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    poly = PolynomialFeatures(degree=2)
    X_2 = poly.fit_transform(X)
    X_2_names = poly.get_feature_names(df.columns[1:])
    mdl = RidgeCV(fit_intercept=False)
    mdl.fit(X_2, y)
    yh_ridge_p2 = mdl.predict(X_2)
    mse_ridge_p2 = mean_squared_error(y, yh_ridge_p2)
    beta = pd.Series(mdl.coef_, index=X_2_names)
    set_trace()


if __name__ == '__main__':
    eda()
    # tr_ridge()