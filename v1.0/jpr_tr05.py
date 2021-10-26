import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from lightgbm import LGBMRegressor
from sklearn.model_selection import GridSearchCV
from joblib import dump, load
from pdb import set_trace


def lgbt_gscv():
    df = pd.read_parquet("qsa_lrp2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    poly = PolynomialFeatures(degree=2)
    X_2 = poly.fit_transform(X)
    n_e, n_l, lr = [10, 20, 50, 100, 200, 500], [10, 100, 1000, 10000], [0.001, 0.01, 0.1]
    param = {'num_leaves': n_l, 'learning_rate': lr, 'n_estimators': n_e}
    mdl = LGBMRegressor(random_state=0)
    gs = GridSearchCV(mdl, param, scoring='neg_mean_squared_error', n_jobs=-1, cv=10, verbose=10,
                      return_train_score=True)
    gs.fit(X=X_2, y=y)
    rst = pd.DataFrame(gs.cv_results_)
    rst.to_csv('gscv_lgbt.csv')


if __name__ == '__main__':
    lgbt_gscv()
