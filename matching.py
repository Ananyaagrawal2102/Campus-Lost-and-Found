
import pandas as pd

from database import load_items


# ==========================================
# TEXT NORMALIZATION
# ==========================================

def normalize(value):

    if pd.isna(value):
        return ""

    return str(value).strip().casefold()


# ==========================================
# CALCULATE MATCH SCORE
# ==========================================

def calculate_match_score(lost_item, found_item):

    score = 0
    total_weight = 0

    weights = {
        "Name": 30,
        "Category": 20,
        "Colour": 20,
        "Location": 20,
        "Date": 10
    }

    for field, weight in weights.items():

        lost_value = normalize(lost_item[field])
        found_value = normalize(found_item[field])

        # Ignore fields where information is missing
        if not lost_value or not found_value:
            continue

        total_weight += weight

        if lost_value == found_value:
            score += weight

    if total_weight == 0:
        return 0

    percentage = (score / total_weight) * 100

    return round(percentage)


# ==========================================
# FIND MATCHING ITEMS
# ==========================================

def find_matches(lost_item_id):

    lost_items = load_items("lost")
    found_items = load_items("found")

    selected_item = lost_items[
        lost_items["ID"] == lost_item_id
    ]

    if selected_item.empty:
        return []

    lost_item = selected_item.iloc[0]

    # Do not match an item already returned
    if normalize(lost_item["Status"]) != "open":
        return []

    matches = []

    for _, found_item in found_items.iterrows():

        # Only consider found items that are still open
        if normalize(found_item["Status"]) != "open":
            continue

        score = calculate_match_score(
            lost_item,
            found_item
        )

        # Keep possible matches with at least 40% similarity
        if score >= 40:

            matches.append({
                "item": found_item.to_dict(),
                "score": score
            })

    # Show highest scoring matches first
    matches.sort(
        key=lambda match: match["score"],
        reverse=True
    )

    return matches
