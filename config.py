import os


class FlaskConfig:
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))

class CeleryConfig:
    broker_url="redis://localhost"
    result_backend="redis://localhost"