import os


class FlaskConfig:
    ENV = os.environ.get("ENV", "development")
    DEBUG = os.environ.get("DEBUG", "True") == "True"
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))

class CeleryConfig:
    broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost")
    result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost")