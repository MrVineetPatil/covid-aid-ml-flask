import os
from flask import Flask, request, jsonify

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json(force=True)
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {data}."


