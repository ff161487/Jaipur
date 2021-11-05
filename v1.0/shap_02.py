import pandas as pd
import matplotlib.pyplot as plt
import shap
from sklearn.preprocessing import PolynomialFeatures
from joblib import load
from pdb import set_trace


def shap_plot():
    mdl = load("lgbm_p2.joblib")
    df = pd.read_parquet("qsa_lgbm_p2.pqt")
    X, y = df.iloc[:, 1:].to_numpy(), df.iloc[:, 0].to_numpy()

    # Transform features
    poly = PolynomialFeatures(degree=2)
    X_2 = poly.fit_transform(X)
    X_2_names = poly.get_feature_names(input_features=df.columns[1:])

    # Explain the model's predictions using SHAP
    print("Finish loading model. Begin computing SHAP values...")
    explainer = shap.TreeExplainer(mdl.named_steps['lgbm'], masker=X_2)
    shap_values = explainer.shap_values(X_2)

    # Summarize the effects of all the features
    print("Visualizing SHAP values...")
    shap.summary_plot(shap_values, X_2, feature_names=X_2_names)
    plt.show()
    set_trace()


if __name__ == '__main__':
    shap_plot()

