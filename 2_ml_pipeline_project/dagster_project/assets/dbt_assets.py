import subprocess
from dagster import asset
from dagster_project.assets.airbyte_assets import sync_airbyte_connection

@asset(deps=[sync_airbyte_connection])
def run_dbt():
    try:
        subprocess.run(["dbt", "run", "--project-dir", "dbt"], check=True)
        print("[DBT] Ejecución exitosa")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"[DBT] Error ejecutando dbt run: {e}")

        raise RuntimeError(f"[DBT] Error ejecutando dbt run: {e}")
