from flask import Flask, render_template, request, flash
from math_ops import add, subtract, multiply, divide

app = Flask(__name__)
app.secret_key = "change-me-to-a-random-value"

operations = {
    "add": ("Add", add),
    "subtract": ("Subtract", subtract),
    "multiply": ("Multiply", multiply),
    "divide": ("Divide", divide),
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        op = request.form.get("operation")
        try:
            a = float(request.form.get("a", ""))
            b = float(request.form.get("b", ""))
        except ValueError:
            error = "Please enter valid numbers."
        else:
            name, func = operations.get(op, (None, None))
            if func is None:
                error = "Unknown operation"
            else:
                try:
                    result = func(a, b)
                except Exception as exc:
                    error = str(exc)
    return render_template("index.html", operations=operations, result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
