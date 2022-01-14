import time

from trie import Trie, make_from_file
from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from flask_restful import Resource
from flask import request


app = Flask(__name__, static_url_path='', static_folder='frontend/my-app/build')
api = Api(app)
CORS(app)

root = make_from_file('./dictionary.txt')

@app.route("/")
def start():
    return send_from_directory(app.static_folder, 'index.html')


class Search(Resource):

    def post(self):
        jsn = request.get_json()
        query = jsn['query']
        words = root.search(query)
        resp = {'result': words}
        return resp, 201

    def get(self):
        query = request.args.get('query')
        words = root.search(query)
        resp = {'result': words}
        return resp, 201





api.add_resource(Search, '/search')


if __name__ == "__main__":
    app.run(threaded=True, port=5000)

