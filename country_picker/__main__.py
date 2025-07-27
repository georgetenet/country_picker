"""
Entry point for country_picker

Allows package to be run with `python -m country_picker`.
Handles CLI for pre-selecting country.
"""
import argparse
from country_picker.main import run

if __name__ == "__main__":
    # parses arguments
    parser = argparse.ArgumentParser(
        description="A simple app to select a country from a list."
    )
    parser.add_argument(
        "--select",
        type=str,
        metavar="COUNTRY",
        help="The country to pre-select on startup."
    )
    args = parser.parse_args()

    # passes pre-selected country to run function
    run(selected_country=args.select)
