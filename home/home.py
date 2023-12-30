from flask import Blueprint, render_template, redirect, url_for
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

home_bp = Blueprint('home', __name__, template_folder='templates',
    static_folder='static', static_url_path='/static/home')

@home_bp.route('/')
@jwt_required()
def index():

    return render_template('index.html')
