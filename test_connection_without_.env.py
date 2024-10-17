from sqlalchemy import create_engine, text

# Define the PostgreSQL connection string
connection_string = "postgresql://postgres:postgres@localhost:5432/mydb"

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Test the connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    data = result.fetchone()
    print(f"Connection established successfully: {data}")

