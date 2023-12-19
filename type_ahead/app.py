from flask import Flask
from flask import send_from_directory
from flask import request
from trie import Trie

app = Flask(__name__, static_folder='frontend/build')


@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/suggest")
def about():
    query = request.values.get('q')
    trie = Trie()
    suggestions = trie.type_ahead(query)
    return {'suggest': suggestions}

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
