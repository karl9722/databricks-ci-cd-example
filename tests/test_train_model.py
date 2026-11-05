
from notebooks.train_model import train_model


def test_model_training():
    model, accuracy, X_train = train_model()

    assert model is not None
    assert 0 <= accuracy <= 1
    assert accuracy >= 0.80
    assert X_train.shape[1] == 4


def test_model_prediction():
    model, _, X_train = train_model()

    predictions = model.predict(X_train[:5])

    assert len(predictions) == 5
    assert all(pred in [0, 1, 2] for pred in predictions)
