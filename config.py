import os


class FlaskConfig:
    ENV = os.environ.get("ENV", "development")
    DEBUG = os.environ.get("DEBUG", "True") == "True"
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
