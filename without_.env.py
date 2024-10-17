from sqlalchemy import create_engine

# Define the PostgreSQL connection string
connection_string = "postgresql://postgres:postgres@localhost:5432/mydb"

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    print(result.fetchone())
