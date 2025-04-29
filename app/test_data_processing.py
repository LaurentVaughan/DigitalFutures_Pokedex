import pandas as pd
import pytest
from .data_processing import (
    load_and_clean_data,
    clean_numerical_columns,
    clean_categorical_columns,
    convert_data_types,
    drop_unnecessary_columns,
    enrich_dataset,
)


# Sample data for testing
@pytest.fixture
def sample_data():
    data = {
        "PassengerId": [1, 2, 3],
        "Age": [22, None, 35],
        "Fare": [7.25, None, 8.05],
        "Embarked": ["S", None, "C"],
        "Cabin": ["C85", None, "E46"],
        "Sex": ["male", "female", "male"],
        "Pclass": [1, 2, 3],
        "Survived": [1, 0, 1],
        "SibSp": [1, 0, 0],
        "Parch": [0, 1, 0],
        "Ticket": ["A/5 21171", "PC 17599", "STON/O2. 3101282"],
    }
    return pd.DataFrame(data)


@pytest.fixture
def cleaned_numerical_data(sample_data):
    """Fixture for data after cleaning numerical columns."""
    return clean_numerical_columns(sample_data.copy())


@pytest.fixture
def cleaned_categorical_data(sample_data):
    """Fixture for data after cleaning categorical columns."""
    return clean_categorical_columns(sample_data.copy())


@pytest.fixture
def converted_data_types_data(sample_data):
    """
    Fixture for data after converting data types
    Need cleaned data but don't want to rely on other fixtures
    """
    df = sample_data.copy()
    df["Age"] = df["Age"].fillna(df["Age"].mean().round())
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["HasCabin"] = df["Cabin"].notnull().astype(int)
    df.drop(columns=["Cabin"], inplace=True)
    return convert_data_types(df)


@pytest.fixture
def drop_unnecessary_columns_data(sample_data):
    """Fixture for data after dropping unnecessary columns"""
    return drop_unnecessary_columns(sample_data.copy())


@pytest.fixture
def enriched_data(sample_data):
    """Fixture for data after enriching the dataset."""
    return enrich_dataset(sample_data.copy())


@pytest.fixture
def cleaned_data(sample_data, tmp_path):
    """Fixture for data after running load_and_clean_data."""
    filepath = tmp_path / "test_titanic.csv"
    sample_data.to_csv(filepath, index=False)
    return load_and_clean_data(filepath)


# Tests for clean_numerical_columns
def test_clean_numerical_columns_fills_age_no_missing_values(
    cleaned_numerical_data,
):
    assert (
        cleaned_numerical_data["Age"].isnull().sum() == 0
    ), "Age column should have no missing values"


def test_clean_numerical_columns_fills_fare_no_missing_values(
    cleaned_numerical_data,
):
    assert (
        cleaned_numerical_data["Fare"].isnull().sum() == 0
    ), "Fare column should have no missing values"


# Tests for clean_categorical_columns
def test_clean_categorical_columns_fills_embarked_no_missing_values(
    cleaned_categorical_data,
):
    assert (
        cleaned_categorical_data["Embarked"].isnull().sum() == 0
    ), "Embarked column should have no missing values"


def test_clean_categorical_columns_drops_cabin_column(
    cleaned_categorical_data,
):
    assert (
        "Cabin" not in cleaned_categorical_data.columns
    ), "Cabin column should be dropped"


def test_clean_categorical_columns_adds_has_cabin_column(
    cleaned_categorical_data,
):
    assert (
        "HasCabin" in cleaned_categorical_data.columns
    ), "HasCabin column should be added"


def test_clean_categorical_columns_has_cabin_correct_values(
    cleaned_categorical_data,
):
    assert cleaned_categorical_data["HasCabin"].tolist() == [
        1,
        0,
        1,
    ], "HasCabin values should be correct"


# Tests for convert_data_types
def test_convert_data_types_sex_is_category(converted_data_types_data):
    assert (
        converted_data_types_data["Sex"].dtype.name == "category"
    ), "Sex column should be of type category"


def test_convert_data_types_embarked_is_category(converted_data_types_data):
    assert (
        converted_data_types_data["Embarked"].dtype.name == "category"
    ), "Embarked column should be of type category"


def test_convert_data_types_pclass_is_category(converted_data_types_data):
    assert (
        converted_data_types_data["Pclass"].dtype.name == "category"
    ), "Pclass column should be of type category"


def test_convert_data_types_survived_is_bool(converted_data_types_data):
    assert (
        converted_data_types_data["Survived"].dtype.name == "bool"
    ), "Survived column should be of type bool"


def test_convert_data_types_age_is_integer(converted_data_types_data):
    assert pd.api.types.is_integer_dtype(
        converted_data_types_data["Age"]
    ), "Age column should be of integer type"


def test_convert_data_types_fare_is_float(converted_data_types_data):
    assert pd.api.types.is_float_dtype(
        converted_data_types_data["Fare"]
    ), "Fare column should be of float type"


# Tests for drop_unnecessary_columns
def test_drop_unnecessary_columns_removes_ticket(
    drop_unnecessary_columns_data,
):
    assert (
        "Ticket" not in drop_unnecessary_columns_data.columns
    ), "Ticket column should be dropped"


def test_drop_unnecessary_columns_removes_duplicates(
    drop_unnecessary_columns_data,
):
    assert (
        drop_unnecessary_columns_data.duplicated().sum() == 0
    ), "There should be no duplicate rows"


# Tests for enrich_dataset
def test_enrich_dataset_adds_family_size(enriched_data):
    assert (
        "FamilySize" in enriched_data.columns
    ), "FamilySize column should be added"


def test_enrich_dataset_family_size_values(enriched_data):
    assert enriched_data["FamilySize"].tolist() == [
        2,
        2,
        1,
    ], "FamilySize values should be correct"


def test_enrich_dataset_adds_age_group(enriched_data):
    assert (
        "AgeGroup" in enriched_data.columns
    ), "AgeGroup column should be added"


def test_enrich_dataset_age_group_is_category(enriched_data):
    assert (
        enriched_data["AgeGroup"].dtype.name == "category"
    ), "AgeGroup column should be of type category"


def test_load_and_clean_data_no_missing_values(cleaned_data):
    assert (
        not cleaned_data.isnull().values.any()
    ), "There should be no missing values after cleaning"


def test_load_and_clean_data_adds_family_size_column(cleaned_data):
    assert (
        "FamilySize" in cleaned_data.columns
    ), "FamilySize column should be added"


def test_load_and_clean_data_adds_age_group_column(cleaned_data):
    assert (
        "AgeGroup" in cleaned_data.columns
    ), "AgeGroup column should be added"


def test_load_and_clean_data_drops_ticket_column(cleaned_data):
    assert (
        "Ticket" not in cleaned_data.columns
    ), "Ticket column should be dropped"
