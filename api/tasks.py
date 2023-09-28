from celery import shared_task
from api.gm03_validator import gm03_validator

@shared_task(bind=True)
def validate(self, files: list):

    self.update_state(state='RUNNING', meta={'progress': 0})

    result = []
    progress = 0

    for file in files:
        result.append(gm03_validator.validate(file))

        progress += 1
        self.update_state(state='RUNNING',
                          meta={'progress': int(round((progress/len(files))*100, 1))})

    return result
