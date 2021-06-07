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
    #data = request.args.get(force=True)
    secret_key = app.config.get("SECRET_KEY")
    prediction = model.predict([np.array([request.args.get('Contact with confirmed'),
                                          request.args.get('Headache'),
                                          request.args.get('Sore throat'),
                                          request.args.get('Shortness of breath'),
                                          request.args.get('Cough'),
                                          request.args.get('Fever'),
                                          request.args.get('Male'),
                                          request.args.get('Age')])])
    if prediction[0]<0.20:
        output =float(prediction[0])*100
    else:
        output =float(prediction[0])*300
    return jsonify(f"The probability of being COVID +VE is {round(output)} %")


