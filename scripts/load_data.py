import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

user = os.getenv("MYSQL_USER")
password = quote_plus(os.getenv("MYSQL_PASSWORD"))  # encode special chars
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DB", "superstore")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# File paths (since your CSVs are in the same folder as load_data.py)
orders_csv = "Orders.csv"
returns_csv = "Returns.csv"
people_csv = "People.csv"

# Load CSVs
pd.read_csv(orders_csv).to_sql("orders_raw", con=engine, if_exists="replace", index=False)
pd.read_csv(returns_csv).to_sql("returns_raw", con=engine, if_exists="replace", index=False)
pd.read_csv(people_csv).to_sql("people_raw", con=engine, if_exists="replace", index=False)

print("🎉 All CSVs loaded successfully!")
