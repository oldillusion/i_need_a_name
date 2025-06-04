from flask import Flask, send_from_directory
import json
import os

app = Flask(__name__, static_folder='public')

# Load data from words.json
with open('resources/words.json') as f:
    words_data = json.load(f)

@app.route('/')
def serve_static():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api')
def api():
    return words_data.get("word", "No word found")

if __name__ == '__main__':
    app.run(debug=True)