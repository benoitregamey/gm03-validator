import flask
from __init__ import create_app
from flask_jwt_extended import JWTManager

app = create_app()
jwt = JWTManager(app)

@jwt.invalid_token_loader
def invalid_token_callback(msg):
    return flask.redirect(flask.url_for('login.login'))

@jwt.unauthorized_loader
def token_not_found_callback(msg):
    return flask.redirect(flask.url_for('login.login'))

if __name__ == "__main__":
    app.run()
