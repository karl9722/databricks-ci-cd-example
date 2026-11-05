
import mlflow
import mlflow.sklearn

from mlflow.models import infer_signature
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100, random_state=42
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy, X_train


def main():
    model, accuracy, X_train = train_model()

    mlflow.set_registry_uri("databricks-uc")
    mlflow.set_experiment("/Shared/iris-ci-cd-experiment")
    
    signature = infer_signature(
        X_train, model.predict(X_train)
    )

    with mlflow.start_run():
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy)

        model_info = mlflow.sklearn.log_model(
            sk_model=model,
            name="random_forest_model",
            signature=signature,
            input_example=X_train[:5]
        )

    registered = mlflow.register_model(
        model_uri=model_info.model_uri,
        name="workspace.default.IrisRFModel"
    )

    print("Accuracy :", accuracy)
    print("Modele :", registered.name)
    print("Version :", registered.version)


if __name__ == "__main__":
    main()
