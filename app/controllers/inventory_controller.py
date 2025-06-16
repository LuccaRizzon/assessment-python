from flask import request, render_template, session
from app.forms.inventory_form import AddProductForm
import re

def handle_inventory_route():
    if "inventory" not in session:
        session["inventory"] = {}

    form = AddProductForm()
    inventory = session["inventory"]
    message = ""
    results = []
    active_tab = "add"

    if request.method == "POST":
        action = request.form.get("action", "").strip()
        active_tab = action 

        if action == "add":
            if form.validate_on_submit():
                name = form.name.data.strip()
                category = form.category.data.strip()
                price = float(form.price.data)
                quantity = int(form.quantity.data)

                if name in inventory:
                    existing = inventory[name]
                    if (existing["category"] == category and 
                        existing["price"] == price and 
                        existing["quantity"] == quantity):
                        message = f"Product '{name}' already exists with same data."
                    else:
                        inventory[name]["quantity"] += quantity
                        message = f"Updated quantity of '{name}'."
                else:
                    inventory[name] = {
                        "category": category,
                        "price": price,
                        "quantity": quantity
                    }
                    message = f"Added new product '{name}'."

                form = AddProductForm(formdata=None)

            else:
                message = "All fields are required and must be valid."

        elif action == "remove":
            name = request.form.get("remove_name", "").strip()
            if name in inventory:
                del inventory[name]
                message = f"Removed product '{name}'."
            else:
                message = f"Product '{name}' not found."

        elif action == "search":
            search_category = request.form.get("search_category", "").strip()
            results = [
                {"name": k, **v}
                for k, v in inventory.items()
                if v["category"].lower() == search_category.lower()
            ]

        elif action == "most_expensive":
            if inventory:
                most_expensive = max(inventory.items(), key=lambda x: x[1]["price"])
                results = [{
                    "name": most_expensive[0],
                    "price": most_expensive[1]["price"]
                }]
            else:
                message = "Inventory is empty."

        elif action == "low_stock":
            try:
                minimum = int(request.form.get("minimum_stock", ""))
                results = [
                    {"name": k, **v}
                    for k, v in inventory.items()
                    if v["quantity"] < minimum
                ]
            except ValueError:
                message = "Invalid minimum stock input."

        session["inventory"] = inventory

    return render_template(
        "fifth_challenge.html",
        inventory=inventory,
        results=results,
        message=message,
        active_tab=active_tab,
        form=form
    )
