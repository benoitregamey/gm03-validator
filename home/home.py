import os
import shutil
from datetime import datetime
from flask import Blueprint, render_template
from flask import request
from werkzeug.utils import secure_filename
from home.gm03_checker import gm03_check

home_bp = Blueprint('home', __name__, template_folder='templates',
    static_folder='static', static_url_path='/static/home')

@home_bp.route('/')
def index():

    return render_template('index.html')

@home_bp.route('/upload', methods=['POST'])
def upload():

    temp_dir = f"home/static/{datetime.today().strftime('%Y%m%d%H%M%S%f')}"
    os.mkdir(temp_dir)

    files = request.files.getlist('files')
    for file in files:
        file.save(os.path.join(temp_dir, secure_filename(file.filename)))
    
    results = gm03_check(temp_dir)
    shutil.rmtree(temp_dir)

    return results