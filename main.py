from flask import Flask, send_from_directory, jsonify
from app.name_data import NameData

app = Flask(__name__, static_folder='public')

# Load JSON data using NameData class
name_data = NameData('resources/nouns.json', 'resources/adjectives.json')

# API routes
@app.route('/api/name', methods=['GET'])
def api():
    return jsonify({"name": name_data.generate_random_name()})

# Attempt to serve any remaining routes as static files
@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def serve_static(u_path):
    return app.send_static_file(u_path)

if __name__ == '__main__':
    app.run(debug=True)