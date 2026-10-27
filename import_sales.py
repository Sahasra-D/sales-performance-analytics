
import pandas as pd
import mysql.connector
from getpass import getpass

file_path = (
    r"C:\Users\D Sahasra\OneDrive\Desktop"
    r"\Sales_Performance_Analytic_Dashboard_Project"
    r"\data\cleaned_sales_data.csv"
)

df = pd.read_csv(file_path, dtype={"Postal Code": "string"})

if "Subcategory" in df.columns and "Sub-Category" not in df.columns:
    df.rename(columns={"Subcategory": "Sub-Category"}, inplace=True)

columns = [
    "Row ID", "Order ID", "Order Date", "Ship Date",
    "Ship Mode", "Customer ID", "Customer Name", "Segment",
    "Country", "City", "State", "Postal Code", "Region",
    "Product ID", "Category", "Sub-Category", "Product Name",
    "Sales", "Quantity", "Discount", "Profit"
]

missing = [col for col in columns if col not in df.columns]
if missing:
    raise ValueError(f"Missing CSV columns: {missing}")

df = df[columns].copy()

for col in ["Order Date", "Ship Date"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

df = df.astype(object).where(pd.notna(df), None)

for col in ["Order Date", "Ship Date"]:
    df[col] = df[col].apply(
        lambda x: x.to_pydatetime().date()
        if x is not None else None
    )

df["Postal Code"] = df["Postal Code"].apply(
    lambda x: str(x).strip() if x is not None else None
)

connection = None
cursor = None

try:
    password = getpass("Enter your MySQL root password: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="sales_performance"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM sales")
    existing_rows = cursor.fetchone()[0]

    if existing_rows > 0:
        raise RuntimeError(
            f"The sales table already has {existing_rows} rows. "
            "Import cancelled to avoid duplicates."
        )

    placeholders = ", ".join(["%s"] * len(columns))
    column_names = ", ".join(f"`{col}`" for col in columns)

    query = (
        f"INSERT INTO sales ({column_names}) "
        f"VALUES ({placeholders})"
    )

    records = list(df.itertuples(index=False, name=None))

    cursor.executemany(query, records)
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM sales")
    print("Rows in CSV:", len(df))
    print("Rows imported:", cursor.fetchone()[0])
    print("Import successful!")

except Exception:
    if connection and connection.is_connected():
        connection.rollback()
    raise

finally:
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
