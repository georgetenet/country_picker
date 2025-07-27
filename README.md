# Country Picker

A simple Python GUI application built with PyQt6 that fetches a list of countries from a public API and allows the user to select one. This project was created as a technical exercise.

## Features

* **Simple User Interface:** A clean window with a combobox for country selection and a label to display the choice.
* **Asynchronous Data Fetching:** Fetches country data from the [apicountries.com](https://www.apicountries.com) API in a background thread to keep the UI responsive.
* **Command-Line Argument:** Supports an optional `--select` argument to pre-select a country on startup.
* **Tested Logic:** Includes unit tests for the data parsing and fetching logic using `pytest` and `pytest-mock`.

## Requirements

* Python 3.8+
* PyQt6
* requests
* pytest
* pytest-mock

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/georgetenet/country_picker.git
   cd country_picker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create the environment
   python -m venv .venv
   
   # Activate on Windows
   .\.venv\Scripts\activate
   
   # Activate on macOS/Linux
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   *(A `requirements.txt` file is included)*
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the package from the project's root directory:

```bash
python -m country_picker
```

### Pre-selecting a Country

You can pre-select a country by using the `--select` command-line argument. The name is case-insensitive.

```bash
python -m country_picker --select "Switzerland"
```

## Running the Tests

To run the unit tests, use `pytest`:

```bash
pytest
