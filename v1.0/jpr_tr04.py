import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from pdb import set_trace


def eda():
    df = pd.read_parquet("qsa.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()
    mdl = KNeighborsRegressor(n_neighbors=5)
    mdl.fit(X, y)
    yh_kn = mdl.predict(X)
    mse_kn = mean_squared_error(y, yh_kn)
    set_trace()


if __name__ == '__main__':
    eda()
    # tr_ridge()