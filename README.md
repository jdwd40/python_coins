# Crypto Trading Simulator

This is a simple cryptocurrency trading simulation app built with Flask and PostgreSQL. It is designed to provide a hands-on experience of cryptocurrency trading without the risk of investing real money.

## Project Overview

The Crypto Trading Simulator allows users to:

- Register and manage their accounts.
- Buy and sell virtual cryptocurrencies.
- View their portfolio, including the coins they own and their current value.
- View transaction history.
- Witness simulated real-time changes in cryptocurrency prices.

## Setup & Installation

### Pre-requisites

- Python 3.8+
- PostgreSQL

### Virtual Environment Setup

It's recommended to create a virtual environment to keep the project dependencies isolated from other Python projects.

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

### Running the App

After setting up the environment and database, run the app using the following command:

```bash
python main.py
```

## Testing

Tests are located in the `tests/` directory. Run them using the following command:

```bash
python -m unittest discover tests
```

## Database Setup

1. Install [PostgreSQL](https://www.postgresql.org/) and pgAdmin (or any other database management tool of your choice).
2. Create a new PostgreSQL database for the application.

## Environment Variables

You'll need to set the following environment variables:

- `DATABASE_URL`: Connection string for your PostgreSQL database.

For example:

```
export DATABASE_URL="postgresql://user:password@localhost:5432/database_name"
```

Replace `user`, `password`, `localhost`, `5432`, and `database_name` with your PostgreSQL username, password, host, port, and database name, respectively.

## Project Structure

The project has the following structure:

- `controllers`: Contains the route handlers, where the main application logic resides.
- `models`: Contains the SQLAlchemy models for your PostgreSQL database.
- `utils`: Contains utility functions and classes.

## Running the Application

To run the application, navigate to the project root directory and run the following command:

```
python app.py
```

This will start the Flask application on your localhost.

## Testing

Unit tests are located in the `tests` directory. To run the tests, navigate to the project root directory and run the following command:

```
python -m unittest discover tests
```


## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE.md) file for details.

---

