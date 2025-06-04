from flask import Flask, send_from_directory, jsonify
from app.name_data import NameData

app = Flask(__name__, static_folder='public')

# Load JSON data using NameData class
name_data = NameData('resources/nouns.json', 'resources/adjectives.json')

@app.route('/')
def serve_static():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/name', methods=['GET'])
def api():
    return jsonify({"name": name_data.generate_random_name()})

if __name__ == '__main__':
    app.run(debug=True)