from flask import request, render_template, session, redirect, url_for
from app.scripts.stack import Stack

def handle_stack_route():
    if "stack_items" not in session:
        session["stack_items"] = []

    stack = Stack()
    stack.items = session["stack_items"]

    if request.method == "POST":
        value = request.form.get("value", "").strip()
        if value:
            stack.append(value)
            session["stack_items"] = stack.items
        return redirect(url_for("second_challenge"))

    return render_template("second_challenge.html", items=stack.items, top=stack.peek(), size=stack.size())
