from dagster import Definitions

# Airbyte y DBT
from dagster_project.assets.airbyte_assets import sync_airbyte_connection
from dagster_project.assets.dbt_assets import run_dbt

# Preprocesamiento
from dagster_project.assets.preprocessing_assets import (
    raw_dataframe,
    X_train,
    X_test,
    y_train,
    y_test,
    user2idx,
    movie2idx,
)

# Entrenamiento y Evaluación
from dagster_project.assets.training_assets import keras_model1
from dagster_project.assets.evaluation_assets import evaluate_model

# Job
from dagster_project.jobs.training_job import training_job

defs = Definitions(
    assets=[
        sync_airbyte_connection,
        run_dbt,
        raw_dataframe,
        X_train,
        X_test,
        y_train,
        y_test,
        user2idx,
        movie2idx,
        keras_model1,
        evaluate_model,
    ],
    jobs=[training_job],
)

