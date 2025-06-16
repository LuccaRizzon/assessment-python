from flask import request, render_template

def handle_fibonacci_route():
    result = None
    value = ""

    if request.method == "POST":
        value = request.form.get("number", "")
        if value.isdigit():
            result = fibonacci(int(value))

    return render_template("fourth_challenge.html", result=result, value=value)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
