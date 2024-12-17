import os
from flask import Flask, app
from . import db
from . import auth
from . import blog



def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testinng
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return 'Hello, World!'
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='index')
    return app


