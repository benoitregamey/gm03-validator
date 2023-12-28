from flask import Blueprint, render_template, request, flash, redirect, url_for
import requests
import time

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
            flash("Wrong username or password", "danger")

        else:
            if r.status_code == 200:
                if r.json()["profile"] == "Administrator":
                    return redirect(url_for("home.index"))
                else:
                    flash("You must have an Administrator profile to log in",
                            "danger")
            else:
                flash("Wrong username or password", "danger")

    return render_template('login.html')