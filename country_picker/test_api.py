"""
Tests for the API data parsing logic.
"""
import pytest
import requests
from country_picker.api import parse_countries, get_country_names

@pytest.fixture
def sample_json_data():
    """Provides a sample of the country JSON data for testing."""
    return [
        {"name": "Switzerland", "cca2": "CH"},
        {"name": "Brazil", "cca2": "BR"},
        {"name": "Afghanistan", "cca2": "AF"},
        {"name": None},
        {"cca2": "DE"},
        {"name": ""},
    ]

# --- Tests for the parsing logic ---

def test_parse_countries_sorted_alphabetically(sample_json_data):
    """
    Tests that the parsing function returns a list of names sorted alphabetically
    and correctly filters invalid entries.
    """
    expected = ["Afghanistan", "Brazil", "Switzerland"]
    result = parse_countries(sample_json_data)
    assert result == expected

def test_parse_countries_empty_input():
    """Tests that the parsing function handles an empty list gracefully."""
    assert parse_countries([]) == []

def test_parse_countries_invalid_input():
    """Tests that the parsing function handles non-list input types."""
    assert parse_countries("not a list") == []
    assert parse_countries(None) == []
    assert parse_countries({"key": "value"}) == []

# --- nnew tests for network function ---

def test_get_country_names_success(mocker, sample_json_data):
    """
    Tests get_country_names function on a successful API call.
    Uses mocking to prevent a real network request.
    
    args:
        mocker: The pytest-mock
        sample_json_data: The sample data to be returned by mock.
    """
    # Mock the requests.get call
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = sample_json_data
    
    mocker.patch("requests.get", return_value=mock_response)
    
    # Call the function
    result = get_country_names()
    
    # Assert that the result is what we expect from the parsing logic
    expected = ["Afghanistan", "Brazil", "Switzerland"]
    assert result == expected
    # Optional: Assert that requests.get was called
    requests.get.assert_called_once_with("https://www.apicountries.com/countries", timeout=10)

def test_get_country_names_network_error(mocker):
    """
    Tests the get_country_names function when a network error occurs.
    
    args:
        mocker: The pytest-mock fixture.
    """
    # Configure the mock to raise a RequestException
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException)
    
    # Call the function and assert it returns an empty list
    result = get_country_names()
    assert result == []

