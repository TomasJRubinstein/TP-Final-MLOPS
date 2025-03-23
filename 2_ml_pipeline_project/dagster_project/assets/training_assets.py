import mlflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from dagster import asset


@asset
def keras_model1(X_train, y_train, user2idx, movie2idx):
    num_users = len(user2idx)
    num_movies = len(movie2idx)

    # Entradas
    user_input = keras.Input(shape=(1,), name="user_input")
    movie_input = keras.Input(shape=(1,), name="movie_input")

    # Embeddings
    user_embedding = layers.Embedding(input_dim=num_users, output_dim=16)(user_input)
    movie_embedding = layers.Embedding(input_dim=num_movies, output_dim=16)(movie_input)

    # Dot product
    dot_product = layers.Dot(axes=2)([user_embedding, movie_embedding])
    output = layers.Flatten()(dot_product)

    # Modelo
    model = keras.Model(inputs=[user_input, movie_input], outputs=output)
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])

    # Entrenamiento con MLflow
    with mlflow.start_run(run_name="keras_model1") as run:
        mlflow.log_param("embedding_dim", 16)
        mlflow.log_param("optimizer", "adam")
        mlflow.log_param("loss", "mse")

        model.fit(
            [X_train["user_idx"], X_train["movie_idx"]],
            y_train,
            epochs=5,
            batch_size=32,
            verbose=1
        )

        mlflow.keras.log_model(model, artifact_path="model", registered_model_name="keras_recommender")
        model_uri = f"runs:/{run.info.run_id}/model"

    return model_uri

