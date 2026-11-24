
from database import load_items


# ==========================================
# SEARCH ITEMS
# ==========================================

def search_items(item_type, keyword):

    df = load_items(item_type)

    keyword = str(keyword).strip().casefold()

    # Return all records if search is empty
    if not keyword:
        return df

    # Fields in which the search will be performed
    columns = [
        "Name",
        "Category",
        "Colour",
        "Location"
    ]

    # Replace missing values with empty strings
    searchable_data = df[columns].fillna("")

    # Compare the keyword with all selected columns
    mask = searchable_data.apply(
        lambda column: column.astype(str).str.casefold().str.contains(
            keyword,
            regex=False
        )
    ).any(axis=1)

    # Return only matching records
    return df[mask]
