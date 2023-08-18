from flask import Flask
from celery import Celery, Task

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.FlaskConfig')  # configure app using the Config class defined in config.py

    with app.app_context():

        from home.home import home_bp
        app.register_blueprint(home_bp)

        from api.api import api_bp
        app.register_blueprint(api_bp)

        celery_init_app(app)

        return app


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object('config.CeleryConfig')
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app