
import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    # Charger les donnees
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Diviser les donnees
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Entrainer le modele
    model = RandomForestClassifier(
        n_estimators=100, random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluer le modele
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Accuracy du modele : {accuracy:.4f}")

    # Enregistrer les resultats avec MLflow
    with mlflow.start_run():
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(
            model, name="random_forest_model"
        )


if __name__ == "__main__":
    main()
