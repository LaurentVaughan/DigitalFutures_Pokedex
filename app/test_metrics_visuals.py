import pytest
import pandas as pd
from unittest.mock import patch
from app.metrics_visuals import (
    calculate_total_passengers,
    calculate_overall_survival_rate,
    calculate_average_age,
    calculate_survival_rate_by_gender,
    create_survival_rate_by_gender_chart,
    create_age_distribution_histogram,
    display_metrics,
    display_visualizations,
)


# Fixture for sample DataFrame
@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "PassengerId": [1, 2, 3, 4],
            "Survived": [1, 0, 1, 0],
            "Age": [22, 35, 28, 40],
            "Sex": ["male", "female", "male", "female"],
        }
    )


# Test for calculate_total_passengers
def test_calculate_total_passengers(sample_df):
    result = calculate_total_passengers(sample_df)
    assert result == 4, "Total passengers should be 4"


# Test for calculate_overall_survival_rate
def test_calculate_overall_survival_rate(sample_df):
    result = calculate_overall_survival_rate(sample_df)
    assert result == 0.5, "Overall survival rate should be 0.5"


# Test for calculate_average_age
def test_calculate_average_age(sample_df):
    result = calculate_average_age(sample_df)
    assert result == 31.25, "Average age should be 31.25"


# Test for calculate_survival_rate_by_gender
def test_calculate_survival_rate_by_gender(sample_df):
    result = calculate_survival_rate_by_gender(sample_df)
    expected = pd.Series({"male": 1.0, "female": 0.0}, name="Survived")
    expected.index.name = "Sex"  # Set the index name to match the result
    # Sort both Series by index before comparison
    pd.testing.assert_series_equal(
        result.sort_index(), expected.sort_index(), check_dtype=False
    )


# Test for create_survival_rate_by_gender_chart
@patch("app.metrics_visuals.px.bar")
def test_create_survival_rate_by_gender_chart(mock_px_bar, sample_df):
    create_survival_rate_by_gender_chart(sample_df)
    mock_px_bar.assert_called_once()


# Test for create_age_distribution_histogram
@patch("app.metrics_visuals.px.histogram")
def test_create_age_distribution_histogram(mock_px_histogram, sample_df):
    create_age_distribution_histogram(sample_df)
    mock_px_histogram.assert_called_once()


# Test for display_metrics
@patch("app.metrics_visuals.st.metric")
def test_display_metrics(mock_st_metric, sample_df):
    display_metrics(sample_df)
    assert mock_st_metric.call_count == 5, "Should display 5 metrics"


# Test for display_visualizations
@patch("app.metrics_visuals.st.plotly_chart")
def test_display_visualizations(mock_st_plotly_chart, sample_df):
    display_visualizations(sample_df)
    assert (
        mock_st_plotly_chart.call_count == 2
    ), "Should display 2 visualizations"
