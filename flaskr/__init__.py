# import sys
# sys.path.append("./flaskr")

from flask import Flask
from flask_cors import CORS
from flaskr.Controllers.api import CardPool, Card
from flaskr.Config import Config

def create_app():
    app = Flask(__name__)
    app.debug = Config.DEBUG
    app.config['TESTING'] = Config.TESTING
    app.config['SECRET_KEY'] = Config.secretKey
    
    CORS(app, resources={
        r"/api/*": {
            'origins': [
                'http://localhost:8080',
                'https://jack850628.github.io/'
            ]
        }
    }) 

    CardPool.init_app(app)
    Card.init_app(app)


    @app.route("/")
    def hello():
        # from tasks import CreateThumbnail as task
        # task.hello.delay("安安")
        return "安安"

    return app