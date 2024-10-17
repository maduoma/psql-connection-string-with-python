import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get connection string from environment variable
connection_string = os.getenv("DATABASE_URL")

if connection_string is None:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    data = result.fetchone()
    print(f"Connection established successfully: {data}")
