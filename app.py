
from flask import Flask, render_template, request, redirect, url_for, flash

from database import initialize_database, load_items
from registration import register_item
from search import search_items
from matching import find_matches
from records import get_all_records, mark_as_returned


app = Flask(__name__)

app.secret_key = "campus_lost_found_secret_key"

initialize_database()


# ==========================================
# HOME / DASHBOARD
# ==========================================

@app.route("/")
def home():

    lost_items = load_items("lost")
    found_items = load_items("found")

    total_lost = len(lost_items)
    total_found = len(found_items)

    total_recovered = (
        (lost_items["Status"] == "Returned").sum()
        + (found_items["Status"] == "Returned").sum()
    )

    return render_template(
        "dashboard.html",
        total_lost=total_lost,
        total_found=total_found,
        total_recovered=total_recovered
    )


# ==========================================
# REPORT LOST ITEM
# ==========================================

@app.route("/report-lost", methods=["GET", "POST"])
def report_lost():

    if request.method == "POST":

        success, result = register_item(
            "lost",
            request.form.get("name", ""),
            request.form.get("category", ""),
            request.form.get("colour", ""),
            request.form.get("location", ""),
            request.form.get("date", ""),
            request.form.get("description", "")
        )

        if success:
            flash(
                f"Lost item registered successfully! Your ID is {result}",
                "success"
            )
            return redirect(url_for("home"))

        flash(result, "error")

    return render_template("report_lost.html")


# ==========================================
# REPORT FOUND ITEM
# ==========================================

@app.route("/report-found", methods=["GET", "POST"])
def report_found():

    if request.method == "POST":

        success, result = register_item(
            "found",
            request.form.get("name", ""),
            request.form.get("category", ""),
            request.form.get("colour", ""),
            request.form.get("location", ""),
            request.form.get("date", ""),
            request.form.get("description", "")
        )

        if success:
            flash(
                f"Found item registered successfully! Your ID is {result}",
                "success"
            )
            return redirect(url_for("home"))

        flash(result, "error")

    return render_template("report_found.html")


# ==========================================
# BROWSE ALL ITEMS
# ==========================================

@app.route("/browse-items")
def browse_items():

    lost_items = get_all_records("lost")
    found_items = get_all_records("found")

    return render_template(
        "browse_items.html",
        lost_items=lost_items,
        found_items=found_items
    )


# ==========================================
# SEARCH ITEMS
# ==========================================

@app.route("/search")
def search():

    keyword = request.args.get("keyword", "").strip()

    if keyword:

        lost_items = search_items("lost", keyword)
        found_items = search_items("found", keyword)

        searched = True

    else:

        lost_items = load_items("lost").iloc[0:0]
        found_items = load_items("found").iloc[0:0]

        searched = False

    return render_template(
        "search_items.html",
        lost_items=lost_items,
        found_items=found_items,
        keyword=keyword,
        searched=searched
    )


# ==========================================
# SMART ITEM MATCHING
# ==========================================

@app.route("/smart-matching")
def smart_matching():

    lost_items = load_items("lost")

    selected_id = request.args.get("lost_item_id", "")

    matches = []

    searched = False

    if selected_id:
        matches = find_matches(selected_id)
        searched = True

    return render_template(
        "smart_matching.html",
        lost_items=lost_items,
        matches=matches,
        selected_id=selected_id,
        searched=searched
    )


# ==========================================
# MARK ITEM AS RETURNED
# ==========================================

@app.route("/mark-returned", methods=["POST"])
def mark_returned():

    item_type = request.form.get("item_type", "")
    item_id = request.form.get("item_id", "")

    if item_type not in ["lost", "found"]:
        flash("Invalid item type.", "error")
        return redirect(url_for("browse_items"))

    success = mark_as_returned(item_type, item_id)

    if success:
        flash(
            f"Item {item_id} has been marked as returned!",
            "success"
        )
    else:
        flash("Item not found. Please check the item ID.", "error")

    return redirect(url_for("browse_items"))


# ==========================================
# RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
