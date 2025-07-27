"""
Tests for the API data parsing logic.
"""
import pytest
from country_picker.api import parse_countries

@pytest.fixture
def sample_json_data():
    """Provides a sample of the country JSON for testing"""
    return [
        {"name": "Switzerland", "cca2": "CH"},
        {"name": "Brazil", "cca2": "BR"},
        {"name": "Afghanistan", "cca2": "AF"},
        {"name": None},  # Test against missing name
        {"cca2": "DE"},      # Test against missing name key
        {"name": ""},        # Test against empty name
    ]

def test_parse_countries_sorted_alphabetically(sample_json_data):
    """
    Tests that parsing function returns list of names sorted alphabetically
    and filters invalid entries
    """
    expected = ["Afghanistan", "Brazil", "Switzerland"]
    result = parse_countries(sample_json_data)
    assert result == expected

def test_parse_countries_empty_input():
    """
    Tests that parsing function handles empty list
    """
    assert parse_countries([]) == []

def test_parse_countries_invalid_input():
    """
    Tests that parsing function handles non-list input types
    """
    assert parse_countries("not a list") == []
    assert parse_countries(None) == []
    assert parse_countries({"key": "value"}) == []

