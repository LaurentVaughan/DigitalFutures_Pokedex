import pytest
import pandas as pd
from unittest.mock import patch
from app.filters import (
    add_passenger_class_filter,
    add_embarked_port_filter,
    filter_dataframe,
    apply_filters,
)


# Fixture for sample DataFrame
@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "Pclass": [1, 2, 3, 1, 2],
            "Embarked": ["S", "C", "Q", "S", "C"],
            "Name": ["John", "Alice", "Bob", "Eve", "Charlie"],
        }
    )


# Test for add_passenger_class_filter
@patch("app.filters.st.sidebar.multiselect")
def test_add_passenger_class_filter(mock_multiselect, sample_df):
    mock_multiselect.return_value = [1, 2]
    result = add_passenger_class_filter(sample_df)
    mock_multiselect.assert_called_once_with(
        "Select Passenger Class",
        options=[1, 2, 3],
        default=[1, 2, 3],
    )
    assert result == [1, 2]


# Test for add_embarked_port_filter
@patch("app.filters.st.sidebar.multiselect")
def test_add_embarked_port_filter(mock_multiselect, sample_df):
    mock_multiselect.return_value = ["S", "C"]
    result = add_embarked_port_filter(sample_df)
    mock_multiselect.assert_called_once_with(
        "Select Embarked Port",
        options=["C", "Q", "S"],
        default=["C", "Q", "S"],
    )
    assert result == ["S", "C"]


# Test for filter_dataframe
def test_filter_dataframe(sample_df):
    pclass_filter = [1, 2]
    embarked_filter = ["S"]
    result = filter_dataframe(sample_df, pclass_filter, embarked_filter)
    expected = sample_df[
        (sample_df["Pclass"].isin(pclass_filter))
        & (sample_df["Embarked"].isin(embarked_filter))
    ]
    pd.testing.assert_frame_equal(result, expected)


# Test for apply_filters
@patch("app.filters.add_passenger_class_filter")
@patch("app.filters.add_embarked_port_filter")
def test_apply_filters(
    mock_add_embarked_filter, mock_add_pclass_filter, sample_df
):
    mock_add_pclass_filter.return_value = [1]
    mock_add_embarked_filter.return_value = ["S"]
    result = apply_filters(sample_df)
    expected = sample_df[
        (sample_df["Pclass"].isin([1])) & (sample_df["Embarked"].isin(["S"]))
    ]
    pd.testing.assert_frame_equal(result, expected)
    mock_add_pclass_filter.assert_called_once_with(sample_df)
    mock_add_embarked_filter.assert_called_once_with(sample_df)
