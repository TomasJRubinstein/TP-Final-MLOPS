from dagster import define_asset_job

training_job = define_asset_job(
    name="training_job",
    selection=[
        "sync_airbyte_connection",
        "run_dbt",
        "raw_dataframe",
        "keras_model1",
        "evaluate_model"
    ],
)

