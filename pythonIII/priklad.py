from flask import Flask, request, jsonify

app = Flask(__name__)

# Kontrolér č. 1 – základná stránka
@app.route("/")
def home():
    return "<h1>Vitaj na mojom Flask serveri!</h1><h2>Toto je moj server</h2"

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
    app.run(host="0.0.0.0", port=5000, debug=True)