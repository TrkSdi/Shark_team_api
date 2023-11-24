import os
#from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
#load_dotenv()

connector = "mysql+pymysql"
user = "root"
password = "George"
host = "localhost"
database = "librairie"

ENGINE = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
