import pytest
# TODO: add necessary import

import os
import pandas as pd


@pytest.fixture(scope="session")
def dataset():
    """
    Load the dataset
    """
    data_path = os.path.join("", "data", "census.csv")
    df = pd.read_csv(data_path) # your code here
    return df

# TODO: implement the first test. Change the function name and input as needed
def test_data_lenght(dataset):
    """
    # Test to make sure we have enough data to continue
    """
    # Your code here
    #pass
    assert dataset.shape[0] > 32000


# TODO: implement the second test. Change the function name and input as needed
def test_columns_count(dataset):
    """
    # Test to make sure all the 15 columns are there
    """
    # Your code here
    #pass
    assert dataset.shape[1] == 15


# TODO: implement the third test. Change the function name and input as needed
def test_columns_check(dataset):
    """
    # Test to make sure the model used is Logistical Regression
    """
    # Your code here
    #pass
    #assert isinstance(preds,np.ndarray)
    correct_columns = [
     "age",
     "workclass",
     "fnlgt",
     "education",
     "education-num",
     "marital-status",
     "occupation",
     "relationship",
     "race",
     "sex",
     "capital-gain",
     "capital-loss",
     "hours-per-week",
     "native-country",
     "salary",
     ]
    df_columns = dataset.columns.values
    assert list(correct_columns) == list(df_columns)
