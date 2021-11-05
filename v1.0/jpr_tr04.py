import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge
from joblib import dump
from pdb import set_trace


def kr_p2_gscv():
    df = pd.read_parquet("qsa_lgbm_p2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    param = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100], 'coef0': [0, 1]}
    mdl = KernelRidge(kernel='poly', degree=2)
    gs = GridSearchCV(mdl, param, scoring='neg_mean_squared_error', n_jobs=18, cv=10, verbose=10,
                      return_train_score=True)
    gs.fit(X=X, y=y)
    rst = pd.DataFrame(gs.cv_results_)
    rst.to_csv('gscv_kr_p2.csv')


def tr_kr_p2():
    df = pd.read_parquet("qsa_lgbm_p2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    mdl = KernelRidge(random_state=0, max_depth=15, min_samples_leaf=1e-5)
    mdl.fit(X, y)
    dump(mdl, "kr_p2.joblib")


if __name__ == '__main__':
    kr_p2_gscv()
    # tr_ridge()