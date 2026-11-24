
from database import save_item


def register_item(item_type, name, category, colour,
                  location, date, description):

    # Remove extra spaces from text inputs
    name = name.strip()
    category = category.strip()
    colour = colour.strip()
    location = location.strip()
    date = date.strip()
    description = description.strip()

    # Check whether the item type is valid
    if item_type not in ["lost", "found"]:
        return False, "Invalid item type."

    # Check whether required fields are empty
    if not name or not category or not location or not date:
        return False, "Please fill all required fields."

    # Prepare item information
    item = {
        "Name": name,
        "Category": category,
        "Colour": colour,
        "Location": location,
        "Date": date,
        "Description": description
    }

    # Save item in CSV database
    item_id = save_item(item_type, item)

    return True, item_id
