##  Flask aplikácia

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Kontrolér č. 1 – základná stránka
@app.route("/")
def home():
    return "<h1>Vitaj na mojom Flask serveri!</h1>"

# Kontrolér č. 2 – echo API, ktoré prijme JSON a vráti ho späť
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON"}), 400
    return jsonify({
        "message": "Dostal som tvoje dáta.",
        "received": data
    })


@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": a + b})


# Spustenie servera
if __name__ == "__main__":
    app.run(debug=True)
```

---



```python

from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError
from typing import Any, Dict

app = Flask(__name__)

# --- Pydantic modely ---

class EchoModel(BaseModel):
    # Ak nevieš presnú štruktúru, môžeš povoliť akékoľvek dáta:
    # Alebo uprav podľa toho, čo očakávaš
    data: Any

class AddModel(BaseModel):
    a: float
    b: float

# --- Kontroléry ---

@app.route("/")
def home():
    return "<h1>Vitaj na mojom Flask serveri!</h1>"

@app.route("/echo", methods=["POST"])
def echo():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "Missing JSON"}), 400
    try:
        # Zabaliť payload do slovníka pod klúč 'data', aby vyhovoval EchoModel
        model = EchoModel(data=json_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422
    return jsonify({
        "message": "Dostal som tvoje dáta.",
        "received": model.data  # Toto je validované dáta
    })

@app.route("/add", methods=["POST"])
def add_numbers():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "Missing JSON"}), 400
    try:
        model = AddModel(**json_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422
    result = model.a + model.b
    return jsonify({"result": result})

# --- Spustenie servera ---
if __name__ == "__main__":
    app.run(debug=True)


```