from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "1337"
jwt = JWTManager(app)


@app.route("/", methods=["GET"])
def login():
    access_token = create_access_token(identity=0)
    return jsonify(access_token=access_token), 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    if current_user_id == 1:
        return jsonify({"flag": "<flag_text>"}), 200
    return jsonify({"flag": "Unauthorised"}), 200
