import pytest
# TODO: add necessary import
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from model import train_model, compute_model_metrics, inference


@pytest.fixture(scope="session")
def data():
    """
    Load the dataset
    """
    data_path = os.path.join("", "data", "census.csv")
    df = pd.read_csv(data_path) # your code here
    return df

# TODO: implement the first test. Change the function name and input as needed
def test_data_lenght():
    """
    # Test to make sure we have enough data to continue
    """
    # Your code here
    #pass
    assert len(data)>32000


# TODO: implement the second test. Change the function name and input as needed
def test_columns_count():
    """
    # Test to make sure all the 15 columns are there
    """
    # Your code here
    #pass
    assert data.shape[1] == 15


# TODO: implement the third test. Change the function name and input as needed
def test_model(X_train, y_train):
    """
    # Test to make sure the model used is Logistical Regression
    """
    # Your code here
    #pass
    model = train_model(X_train, y_train)
    assert isinstance(model,LogisticRegression)
