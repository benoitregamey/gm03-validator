from celery import shared_task
from werkzeug.datastructures import FileStorage
import api.gm03_validator
import time

@shared_task(bind=True)
def validate(self, files: list):

    self.update_state(state='RUNNING', meta={'progress': 0})

    result = []
    progress = 0

    for file in files:
        time.sleep(0.5)
        result.append(api.gm03_validator.validate(file))

        progress += 1
        self.update_state(state='RUNNING',
                          meta={'progress': int(round((progress/len(files))*100, 1))})

    return result
