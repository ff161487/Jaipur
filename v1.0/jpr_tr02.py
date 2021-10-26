import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from joblib import dump, load
from pdb import set_trace


def rt_gscv():
    df = pd.read_parquet("qsa.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    m_d = [10, 15, 20, 25]
    msl = [1e-7, 1e-6, 1e-5]
    param = {'max_depth': m_d, 'min_samples_leaf': msl}
    mdl = DecisionTreeRegressor(random_state=0)
    gs = GridSearchCV(mdl, param, scoring='neg_mean_squared_error', n_jobs=-1, cv=10, verbose=10,
                      return_train_score=True)
    gs.fit(X=X, y=y)
    rst = pd.DataFrame(gs.cv_results_)
    rst.to_csv('gscv_rt.csv')


def tr_rt():
    df = pd.read_parquet("qsa.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    mdl = DecisionTreeRegressor(random_state=0, max_depth=15, min_samples_leaf=1e-5)
    mdl.fit(X, y)
    dump(mdl, "rt.joblib")


def check():
    mdl = load("rt.joblib")
    fi = mdl.feature_importances_
    set_trace()


def tr_rtp2():
    df = pd.read_parquet("qsa_lrp2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    mdl = Pipeline([('poly', PolynomialFeatures(degree=2)),
                    ('reg_tree', DecisionTreeRegressor(random_state=0, max_depth=15, min_samples_leaf=1e-5))])
    mdl.fit(X, y)
    dump(mdl, "rt_p2.joblib")


if __name__ == '__main__':
    tr_rtp2()
    # tr_rt()
    # rt_gscv()