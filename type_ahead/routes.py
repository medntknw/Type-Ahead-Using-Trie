from flask import Blueprint
from flask import render_template
from flask import request
from trie import Trie

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    return render_template('base.html')

@bp.route("/suggest")
def about():
    query = request.values.get('q')
    trie = Trie()
    suggestions = trie.type_ahead(query)
    return {'suggest': suggestions}
