# psql-connection-string-with-python 


This project demonstrates how to connect to a PostgreSQL database using Python and SQLAlchemy, with the connection string stored securely in an environment variable.

## Features

- Secure database connection using environment variables
- SQLAlchemy ORM for database operations
- Python-dotenv for loading environment variables
- Psycopg2 as the PostgreSQL adapter for Python

## Prerequisites

- Python 3.7+
- PostgreSQL database

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/psql-connection-string-with-python.git
   cd psql-connection-string-with-python
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your database URL:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/dbname
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ```

## Usage

To run the project, execute the main Python script:
```
python app.py
```

This will start the Flask application and connect to the PostgreSQL database using the connection string from the `.env` file.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
