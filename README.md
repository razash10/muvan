# Muvan Application

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/razash10/muvan.git
    cd muvan
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Run the application:

    ```sh
    python __main__.py
    ```

## Description of the Architecture

### Overview

The Muvan application is designed to provide insights into property leases, including identifying properties with leases about to expire and units with long vacancy periods. The application is built using Flask for the web framework and pandas for data manipulation.

### Components

1. **Flask Application (`__main__.py`)**:
    - Sets up the Flask application and defines the routes for the API endpoints.

2. **Muvan Application (`muvan.py`)**:
    - Contains the `create_app` function that initializes the Flask application and sets up the routes.
    - Routes:
        - `/properties_of_leases_about_to_expire/<int:days>`: Returns properties with leases about to expire in the next specified number of days.
        - `/top_units_with_long_vacancies/<int:count>`: Returns the top units with the longest vacancy periods.

3. **AppState (`app/app_state.py`)**:
    - Manages the state of the application, including loading data from CSV files and providing methods to get insights.

4. **AppStore (`app/app_store.py`)**:
    - Defines the paths to the CSV files and the columns used in the data.
    - Classes:
        - `Paths`: Contains the paths to the CSV files.
        - `Columns`: Contains the column names used in the data.
        - `AppStore`: Combines the `Paths` and `Columns` classes.

### Extensibility

The architecture of the Muvan application supports extensibility in several ways:

1. **Modular Design**:
    - The application is divided into separate modules (`muvan.py`, `app_state.py`, `app_store.py`, and the Flask application), making it easy to add new features or modify existing ones without affecting other parts of the codebase.

2. **Data Loading and Processing**:
    - The `AppState` class handles data loading and processing, making it easy to extend the data processing logic. For example, you can add new methods to calculate additional insights or modify the existing methods to include more complex calculations.

3. **Configuration Management**:
    - The `AppStore` class centralizes the configuration of paths and column names, making it easy to update the configuration without changing the code in multiple places.

4. **API Endpoints**:
    - The Flask application defines API endpoints that can be easily extended to include new routes. For example, you can add new endpoints to provide additional insights or perform different types of data analysis.

By following these principles, the Muvan application is designed to be flexible and easy to extend, allowing for future growth and adaptation to new requirements.

### JSON Response Examples

#### `/properties_of_leases_about_to_expire/<int:days>`

- **Request**: `GET /properties_of_leases_about_to_expire/30`
- **Response**:
    ```json
    {
        "properties": [3, 5, 6]
    }
    ```

#### `/top_units_with_long_vacancies/<int:count>`

- **Request**: `GET /top_units_with_long_vacancies/5`
- **Response**:
    ```json
    {
        "units": [39, 19, 37, 72, 89]
    }
    ```