"""
Handles fetching and parsing of country data from API.
"""
import requests
import json
from typing import List, Dict, Any

API_URL = "https://www.apicountries.com/countries"

def parse_countries(json_data: List[Dict[str, Any]]) -> List[str]:
    """
    Parses list of country data from JSON, extracting names.

    args:
        json_data: list of dictionaries each containing name of country

    returns:
        sorted country list.
    """
    if not isinstance(json_data, list):
        return []
    
    # extract country name
    names = [
        country.get("name") for country in json_data 
        if isinstance(country.get("name"), str) and country.get("name")
    ]
    return sorted(names)

def get_country_names() -> List[str]:
    """
    fetches country data from api returns sorted list of names.

    returns:
        A list of country names, sorted alphabetically. Returns an empty
        list if the request fails or parsing is unsuccessful.
    """
    try:
        # timeout
        response = requests.get(API_URL, timeout=10)
        # exception handler
        response.raise_for_status()  
        data = response.json()
        return parse_countries(data)
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        # log error
        print(f"Error fetching or parsing country data: {e}")
        return []
