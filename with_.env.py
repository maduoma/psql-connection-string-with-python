from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Retrieve variables from the .env file
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug_mode = os.getenv('DEBUG')

print(f'Database URL: {database_url}')
print(f'Secret Key: {secret_key}')
print(f'Debug Mode: {debug_mode}')
