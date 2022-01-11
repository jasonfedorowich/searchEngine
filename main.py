# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
import time

from trie import Trie, make_from_file
from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from flask_restful import Resource
from flask import request


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)
CORS(app)


root = make_from_file('./dictionary.txt')

@app.route("/")
def start():
    return f"<p>hello</p>"


class Search(Resource):

    def post(self):
        jsn = request.get_json()
        query = jsn['query']
        words = root.search(query)
        resp = {'result': words}
        return resp, 201




api.add_resource(Search, '/search')


if __name__ == "__main__":
    app.run(threaded=True, port=5000)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
