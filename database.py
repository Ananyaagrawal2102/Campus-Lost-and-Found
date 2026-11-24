
import pandas as pd
from pathlib import Path

# Project ke data folder ka path
DATA_FOLDER = Path(__file__).parent / "data"

# CSV file paths
LOST_FILE = DATA_FOLDER / "lost_items.csv"
FOUND_FILE = DATA_FOLDER / "found_items.csv"

# CSV columns
COLUMNS = [
    "ID",
    "Name",
    "Category",
    "Colour",
    "Location",
    "Date",
    "Description",
    "Status"
]


def initialize_database():

    # Create data folder if it does not exist
    DATA_FOLDER.mkdir(exist_ok=True)

    # Check both CSV files
    for file in [LOST_FILE, FOUND_FILE]:

        if not file.exists() or file.stat().st_size == 0:

            df = pd.DataFrame(columns=COLUMNS)
            df.to_csv(file, index=False)


def load_items(item_type):

    if item_type == "lost":
        file = LOST_FILE

    elif item_type == "found":
        file = FOUND_FILE

    else:
        raise ValueError("Invalid item type")

    return pd.read_csv(file)


def save_item(item_type, item):

    if item_type == "lost":
        file = LOST_FILE
        prefix = "L"

    elif item_type == "found":
        file = FOUND_FILE
        prefix = "F"

    else:
        raise ValueError("Invalid item type")

    df = load_items(item_type)

    # Generate a unique item ID
    new_id = f"{prefix}{len(df) + 1:03d}"

    item["ID"] = new_id
    item["Status"] = "Open"

    # Add new record
    new_row = pd.DataFrame([item])
    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file, index=False)

    return new_id


def update_items(item_type, df):

    if item_type == "lost":
        file = LOST_FILE

    elif item_type == "found":
        file = FOUND_FILE

    else:
        raise ValueError("Invalid item type")

    df.to_csv(file, index=False)
