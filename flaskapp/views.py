from flask import request, jsonify
from config import mycol
from flaskapp import app


@app.route("/get", methods=['GET'])
def get_data():
    output = []
    for i in mycol.find():
        output.append({"name": i["name"], "place": i["place"]})
    return jsonify({"Result": output})

@app.route("/post", methods=["POST"])
def post_data():
    name = request.json["name"]
    place = request.json["place"]
    new_db = mycol.insert({"name": name, "place": place})
    return jsonify(str(new_db))