from flask import Blueprint, request
import api.tasks
from celery.result import AsyncResult

api_bp = Blueprint('api', __name__, static_folder='static',
                   static_url_path='/api/static')

@api_bp.post('/process')
def start_validation():

    files = request.files.getlist('files')
    files = [file.stream.read() for file in files if file.filename.endswith(".xml")]

    task = api.tasks.validate.delay(files)
    return {"uuid": task.id}


@api_bp.get('/process/<uuid>')
def get_validation(uuid: str) -> dict:

    result = AsyncResult(uuid)

    return {
        "state": result.state,
        "progress": "DONE" if result.ready() else result.info["progress"],
        "result": result.result if result.ready() else None,
    }
