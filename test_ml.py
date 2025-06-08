from ml.model import train_model, inference
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def test_model_type():
    """
    This test confirms that train_model returns a randomforestclassifier
    """
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier), "The model is not a RandomForestClassifier"


def test_data_split_size():
    """
    Test that splitting the data produces the expected sizes
    """
    data=pd.read_csv("data/census.csv")
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    number_of_rows = data.shape[0]
    assert len(train) == int(number_of_rows * 0.8)
    assert len(test) == number_of_rows - len(train)

def test_inference_shape():
    """
    Test that inference returns predictions with the correct length
    """
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    model = train_model(X, y)
    preds = inference(model, X)
    assert len(preds) == len(y), "Inference output length does not match"
