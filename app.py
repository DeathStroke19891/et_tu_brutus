from flask import Flask, render_template, make_response
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "1337"
jwt = JWTManager(app)


@app.route("/", methods=["GET"])
def login():
    access_token = create_access_token(identity=0)
    response = make_response(render_template('index.html', token=access_token))
    response.headers['Authorization'] = f'Bearer {access_token}'
    return response

@app.route("/protected", methods=["GET"])
def protected():
    current_user_id = 0
    try:
        current_user_id = get_jwt_identity()
        if current_user_id == 1:
            response = make_response(render_template('protected.html'))
            return response
    except:
        response = make_response(render_template('impaler.html'))
        return response
