import json, random
from flask import Flask, jsonify, request
from PIL import Image 

app = Flask(__name__)

with open("images.json", "r") as f:
    u = json.load(f)

@app.route("/api/images/random", methods=["GET"])
def jokes():
    x = random.randint(0, len(u) - 1)
    y = u[x]
    return jsonify({"url": y})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1000)
