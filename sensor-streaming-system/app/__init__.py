from flask import Flask
import redis

def create_app():
    app = Flask(__name__)
    app.config['REDIS_HOST'] = 'redis'
    app.config['REDIS_PORT'] = 6379
    app.redis = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], decode_responses=True)

    with app.app_context():
        from . import routes

    return app
