from flask import render_template, request, redirect, session
from app import app
from app.scripts.file_processor import process_pld
from app.scripts.stack import Stack
from app.controllers.stack_controller import handle_stack_route
from app.controllers.word_list_controller import handle_word_list_route
from app.controllers.fibonacci_controller import handle_fibonacci_route
from app.controllers.inventory_controller import handle_inventory_route

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first_challenge")
def first_challenge():
    data = process_pld()
    return render_template("first_challenge.html", resultados = data)

@app.route("/second_challenge", methods=["GET", "POST"])
def second_challenge():
    return handle_stack_route()

@app.route("/second_challenge/clear", methods=["POST"])
def clear_stack():
    session.pop("stack_items", None)
    return redirect("/second_challenge")

@app.route("/third_challenge", methods=["GET", "POST"])
def third_challenge():
    return handle_word_list_route()

@app.route("/fourth_challenge", methods=["GET", "POST"])
def fourth_challenge():
    return handle_fibonacci_route()

@app.route("/fifth_challenge", methods=["GET", "POST"])
def fifth_challenge():
    return handle_inventory_route()
