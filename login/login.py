from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import set_access_cookies
import requests

login_bp = Blueprint('login', __name__, template_folder='templates',
    static_folder='static', static_url_path='/static/login')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        session = requests.Session()
        session.auth = (username, password)

        try:

            r = session.get(
                url = "https://www.geocat.ch/geonetwork/srv/api/me",
                headers=headers
            )

            r.raise_for_status()

        except Exception:
            return {}, 403

        else:
            if r.status_code == 200:
                if r.json()["profile"] == "Administrator":
                    response = jsonify({"login": "successful"})
                    access_token = create_access_token(identity=username)
                    set_access_cookies(response, access_token)
                    return response, 200
                else:
                    return {}, 401
            else:
                return {}, 403

    return render_template('login.html')
