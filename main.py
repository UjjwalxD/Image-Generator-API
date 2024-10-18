import json
import random
import logging
from flask import Flask, jsonify, request

class Auth:
    password = "xyz12345"

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

with open("images.json", "r") as file:
    img = json.load(file)

@app.route("/api/images/random", methods=["GET"])
def imgss() -> jsonify:
    password = request.args.get('password')
    if password != Auth.password:
        return jsonify({"error": "Unauthorized access"}), 401

    if not img:
        app.logger.error("Api Error, Images not found :(.")
        return jsonify({"error": "No images available"}), 500
    x = random.randint(0, len(img) - 1)
    ok = img[x]
    app.logger.info("Success")
    return jsonify({"url": ok})

@app.errorhandler(404)
def not_found(error) -> jsonify:
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def internal_error(error) -> jsonify:
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1000)
