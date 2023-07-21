from flask import Flask

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')  # configure app using the Config class defined in config.py

    with app.app_context():

        from home.home import home_bp
        app.register_blueprint(home_bp)

        return app