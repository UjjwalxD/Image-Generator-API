import json, random
from flask import Flask, jsonify, request
from PIL import Image 

app = Flask(__name__)

with open("images.json", "r") as f:
    image_urls = json.load(f)

@app.route("/api/images/random", methods=["GET"])
def get_random_image():
    """Returns a random image URL from the JSON file."""

    random_index = random.randint(0, len(image_urls) - 1)
    random_image_url = image_urls[random_index]
    return jsonify({"url": random_image_url})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
