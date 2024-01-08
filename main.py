from flask import Flask, jsonify
import json
import os


app = Flask(__name__)

with open('jokes.json', 'r', encoding='utf-8') as file:
    total = json.load(file)
    
    
@app.route('/jokes/<int:amount>', methods=['GET'])
def get_jokes(amount):
    if amount < 1:
        return jsonify({"error": "Jokes amount should be in positive int."}), 400

    e = len(total)
    if amount > e:
        return jsonify({"error": f"Only {e} jokes available."}), 400

    s = total[:amount]
    return jsonify({"Sucessfully Generated": s})

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, port=port)