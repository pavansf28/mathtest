# MathTest

Small project demonstrating math operations with both CLI and a web UI.

## Setup

```bash
cd mathtest
python -m venv venv          # optional but recommended
# activate venv (Windows): venv\Scripts\activate
pip install -r requirements.txt
```

## CLI Usage

```bash
python math_test.py
```

Follow the menu to select an operation and enter numbers.

## Web UI

Start the Flask server:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser and interact with the math functions.

## VS Code Plugin

For building the web interface you don't need a special plugin – any HTML/CSS editor will do.  If you want live preview inside VS Code install the **Live Server** extension.

Flask handles routing and rendering the template for you.  The math functions live in `math_ops.py` and are reused by both the CLI and web code.
