from flask import Flask, jsonify
from utils import find_by_id

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/<id>')
def get_info_about_pet(id):
    return find_by_id(id)


if __name__ == "__main__":
    app.run(debug=True)
