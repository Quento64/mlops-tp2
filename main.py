import mlflow
from mlflow.models import infer_signature

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def create_model():
    X = pd.read_csv("winequality-white.csv", sep=';')
    y = X['quality']
    X = X.drop(columns='quality')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    params = {
        "max_iter": 1000,
        "random_state": 42
    }

    model = LogisticRegression(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    mlflow.set_tracking_uri(uri="http://localhost:5000")
    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.log_metric("accuracy", accuracy)

        signature = infer_signature(X_train, model.predict(X_train))
        mlflow.sklearn.log_model(
            sk_model=model,
            signature=signature,
            input_example=X_train,
            registered_model_name="whine_quality"
        )

if __name__ == "__main__":
    create_model()