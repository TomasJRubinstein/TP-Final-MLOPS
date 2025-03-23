import mlflow
from sklearn.metrics import mean_squared_error, mean_absolute_error
from dagster import asset
import pandas as pd


@asset
def evaluate_model(keras_model1, X_test, y_test):
    # Cargar el modelo desde el registry de MLflow
    model = mlflow.keras.load_model(keras_model1)

    # Predicciones
    y_pred = model.predict([X_test["user_idx"], X_test["movie_idx"]])

    # Métricas
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    # Logging en MLflow
    with mlflow.start_run(run_name="evaluate_model") as run:
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("mae", mae)

    print(f"[EVAL] MSE: {mse:.4f} | MAE: {mae:.4f}")

