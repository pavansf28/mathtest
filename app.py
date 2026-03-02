from flask import Flask, render_template, request, flash, jsonify
import random
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


@app.route("/quiz")
def quiz():
    """Serve the interactive math quiz for kids."""
    return render_template("quiz.html", operations=operations)


@app.route("/api/quiz/check", methods=["POST"])
def check_answer():
    """API endpoint to check quiz answers."""
    data = request.get_json()
    op = data.get("operation")
    try:
        a = float(data.get("a", ""))
        b = float(data.get("b", ""))
        user_answer = float(data.get("answer", ""))
    except (ValueError, TypeError):
        return jsonify({"correct": False, "message": "Invalid input!"}), 400
    
    name, func = operations.get(op, (None, None))
    if func is None:
        return jsonify({"correct": False, "message": "Unknown operation"}), 400
    
    try:
        correct_answer = func(a, b)
        # Allow small floating point tolerance
        is_correct = abs(user_answer - correct_answer) < 0.001
        return jsonify({
            "correct": is_correct,
            "correct_answer": correct_answer,
            "user_answer": user_answer
        })
    except Exception as exc:
        return jsonify({"correct": False, "message": str(exc)}), 400


if __name__ == "__main__":
    app.run(debug=True)
