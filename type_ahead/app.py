from flask import Flask
from flask import send_from_directory
from flask import request
from trie import Trie

app = Flask(__name__, static_folder='frontend/build')


@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api/suggest", methods=['GET', 'POST'])
def suggest():
    trie = Trie()
    print('Using trie: %s' % trie)
    if request.method == 'GET':
        query = request.values.get('q')
        if not query:
            return {'suggest': [], 'ok': True, 'msg': 'There is no query!'}
        suggestions = trie.type_ahead(query)
        return {'suggest': suggestions, 'ok': True}

    if request.method == 'POST':
        data = request.get_json()
        key = data.get('query')
        if not key:
            return {'ok': False}, 400
        trie.insert_key(key)
        print(f'Successfully inserted {key} in {trie}')
        return {'ok': True}, 201

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
