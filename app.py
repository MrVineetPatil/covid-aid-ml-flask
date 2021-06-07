import os
import numpy as np
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)
model = pickle.load(open('finalized_model.sav', 'rb'))
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json(force=True)
    secret_key = app.config.get("SECRET_KEY")
    prediction = model.predict([np.array([data['Contact with confirmed'],
                                          data['Headache'],
                                          data['Sore throat'],
                                          data['Shortness of breath'],
                                          data['Cough'],
                                          data['Fever'],
                                          data['Male'],
                                          data['Age 60+']])])
    output = prediction[0]
    return f"The configured secret key is {output}."


