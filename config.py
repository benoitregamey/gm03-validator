import os


class FlaskConfig:
    ENV = os.environ.get("ENV", "development")
    DEBUG = os.environ.get("DEBUG", "True") == "True"
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", os.urandom(24))
    JWT_TOKEN_LOCATION = os.environ.get("JWT_TOKEN_LOCATION", ["cookies"])
    JWT_COOKIE_SECURE = os.environ.get("JWT_COOKIE_SECURE", False)
