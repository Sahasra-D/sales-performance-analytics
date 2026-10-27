
import pandas as pd
import pytest

COLUMNS = [
    "Row ID", "Order ID", "Order Date", "Ship Date",
    "Ship Mode", "Customer ID", "Customer Name", "Segment",
    "Country", "City", "State", "Postal Code", "Region",
    "Product ID", "Category", "Sub-Category", "Product Name",
    "Sales", "Quantity", "Discount", "Profit"
]


def test_required_columns_are_present():
    df = pd.DataFrame(columns=COLUMNS)
    missing = [col for col in COLUMNS if col not in df.columns]
    assert missing == []


def test_missing_column_is_detected():
    df = pd.DataFrame(columns=[
        col for col in COLUMNS if col != "Profit"
    ])
    missing = [col for col in COLUMNS if col not in df.columns]
    assert missing == ["Profit"]


def test_subcategory_column_can_be_renamed():
    df = pd.DataFrame({"Subcategory": ["Chairs"]})

    if "Subcategory" in df.columns and "Sub-Category" not in df.columns:
        df.rename(columns={"Subcategory": "Sub-Category"}, inplace=True)

    assert "Sub-Category" in df.columns
    assert df["Sub-Category"].iloc[0] == "Chairs"


def test_dates_are_converted_to_datetime():
    df = pd.DataFrame({"Order Date": ["2024-01-15"]})
    df["Order Date"] = pd.to_datetime(
        df["Order Date"], errors="coerce"
    )

    assert pd.api.types.is_datetime64_any_dtype(df["Order Date"])
    assert df["Order Date"].iloc[0] == pd.Timestamp("2024-01-15")
