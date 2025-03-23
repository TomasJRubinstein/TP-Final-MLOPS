import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dagster import asset, Output
from sqlalchemy import create_engine
from dagster_project.assets.airbyte_assets import sync_airbyte_connection
from dagster_project.assets.dbt_assets import run_dbt



def get_pg_engine():
    user = "tomirubinstein@gmail.com"
    password = "airbyte"
    host = "localhost"
    port = 5432
    db = "mlops"
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")


@asset(deps=[sync_airbyte_connection, run_dbt])
def raw_dataframe() -> pd.DataFrame:
    engine = get_pg_engine()
    df = pd.read_sql("SELECT * FROM source.scores_movies_users", engine)
    return df


@asset
def user2idx(raw_dataframe):
    return {id_: idx for idx, id_ in enumerate(raw_dataframe["user_id"].unique())}


@asset
def movie2idx(raw_dataframe):
    return {id_: idx for idx, id_ in enumerate(raw_dataframe["movie_id"].unique())}


@asset
def X_train(raw_dataframe, user2idx, movie2idx):
    df = raw_dataframe.copy()
    df["user_idx"] = df["user_id"].map(user2idx)
    df["movie_idx"] = df["movie_id"].map(movie2idx)
    X = df[["user_idx", "movie_idx"]]
    y = df["rating"]
    X_train, _, _, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train


@asset
def X_test(raw_dataframe, user2idx, movie2idx):
    df = raw_dataframe.copy()
    df["user_idx"] = df["user_id"].map(user2idx)
    df["movie_idx"] = df["movie_id"].map(movie2idx)
    X = df[["user_idx", "movie_idx"]]
    y = df["rating"]
    _, X_test, _, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_test


@asset
def y_train(raw_dataframe):
    y = raw_dataframe["rating"]
    _, _, y_train, _ = train_test_split(
        raw_dataframe[["user_id", "movie_id"]], y, test_size=0.2, random_state=42
    )
    return y_train


@asset
def y_test(raw_dataframe):
    y = raw_dataframe["rating"]
    _, _, _, y_test = train_test_split(
        raw_dataframe[["user_id", "movie_id"]], y, test_size=0.2, random_state=42
    )
    return y_test
