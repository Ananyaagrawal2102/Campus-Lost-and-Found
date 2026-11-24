
from database import load_items, update_items


def get_all_records(item_type):
    return load_items(item_type)


def mark_as_returned(item_type, item_id):

    # Load records from the CSV file
    records = load_items(item_type)

    # Check whether records are available
    if records.empty:
        return False

    # Find the item using its ID
    matching_rows = (
        records["ID"].astype(str).str.strip()
        == str(item_id).strip()
    )

    # Check whether the item exists
    if not matching_rows.any():
        return False

    # Update the item's status
    records.loc[matching_rows, "Status"] = "Returned"

    # Save the updated records
    update_items(item_type, records)

    return True
