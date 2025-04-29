from unittest.mock import patch, MagicMock
import pytest
import app.main as main


@pytest.fixture
def mock_dependencies():
    """Fixture to mock all dependencies used in the main function."""
    with patch("app.main.st.set_page_config") as mock_set_page_config, patch(
        "app.main.st.title"
    ) as mock_title, patch(
        "app.main.load_and_clean_data"
    ) as mock_load_and_clean_data, patch(
        "app.main.apply_filters"
    ) as mock_apply_filters, patch(
        "app.main.display_metrics"
    ) as mock_display_metrics, patch(
        "app.main.display_visualizations"
    ) as mock_display_visualizations:

        # Set up mock return values
        mock_load_and_clean_data.return_value = MagicMock()
        mock_apply_filters.return_value = MagicMock()

        # Yield all mocks for use in tests
        yield {
            "mock_set_page_config": mock_set_page_config,
            "mock_title": mock_title,
            "mock_load_and_clean_data": mock_load_and_clean_data,
            "mock_apply_filters": mock_apply_filters,
            "mock_display_metrics": mock_display_metrics,
            "mock_display_visualizations": mock_display_visualizations,
        }


def test_set_page_config(mock_dependencies):
    main.main()
    mock_dependencies["mock_set_page_config"].assert_called_once_with(
        page_title="Titanic Dashboard",
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="auto",
    )


def test_set_title(mock_dependencies):
    main.main()
    mock_dependencies["mock_title"].assert_called_once_with(
        "Titanic Dataset Explorer"
    )


def test_load_and_clean_data_called(mock_dependencies):
    main.main()
    mock_dependencies["mock_load_and_clean_data"].assert_called_once_with(
        "./synthetic_titanic.csv"
    )


def test_apply_filters_called(mock_dependencies):
    main.main()
    mock_dependencies["mock_apply_filters"].assert_called_once()


def test_display_metrics_called(mock_dependencies):
    main.main()
    mock_dependencies["mock_display_metrics"].assert_called_once()


def test_display_visualizations_called(mock_dependencies):
    main.main()
    mock_dependencies["mock_display_visualizations"].assert_called_once()
