import os
import time
import requests
from dagster import asset

AIRBYTE_CONNECTION_ID = os.environ.get("AIRBYTE_CONNECTION_ID", "537d4434-8548-4987-ae9f-c80dfa7e7b29")

AIRBYTE_CONFIG = {
    "host": os.environ.get("AIRBYTE_HOST", "localhost"),
    "port": os.environ.get("AIRBYTE_PORT", "8000"),
    "username": "tomirubinstein@gmail.com",
    "password": "d2heuTEwVy8jT3P5ETAVVpa0BdhSt06m",
}

def trigger_airbyte_sync(connection_id):
    base_url = f"http://{AIRBYTE_CONFIG['host']}:{AIRBYTE_CONFIG['port']}/api/v1"

    response = requests.post(f"{base_url}/connections/sync", json={"connectionId": connection_id})
    response.raise_for_status()
    job_id = response.json()["job"]["id"]
    print(f"[Airbyte] Sync started, job ID: {job_id}")

    while True:
        status_resp = requests.post(f"{base_url}/jobs/get", json={"id": job_id})
        status = status_resp.json()["job"]["status"]
        if status in ("succeeded", "failed", "cancelled", "incomplete"):
            break
        print(f"[Airbyte] Job {job_id} status: {status}... esperando 10s")
        time.sleep(10)

    if status != "succeeded":
        raise RuntimeError(f"[Airbyte] Sync falló con estado: {status}")
    print(f"[Airbyte] Sync completado OK")


@asset
def sync_airbyte_connection():
    trigger_airbyte_sync(AIRBYTE_CONNECTION_ID)
