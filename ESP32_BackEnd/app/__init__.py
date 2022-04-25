
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import paho.mqtt.client as paho
from configure import *
import logging
from flask_mqtt import Mqtt
import coloredlogs

app = Flask(__name__)
api = Api(app)
coloredlogs.install(level='INFO', fmt = '[%(hostname)s] [%(pathname)s:%(lineno)s - %(funcName)s() ] %(asctime)s %(levelname)s %(message)s' )

"""
Kết nối đến mySQL server
"""
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:123456@localhost/espmqtt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_SIZE'] = 20
db = SQLAlchemy(app)
CORS(app, support_credentials=True)

app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'  
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False


try:
    mqtt = Mqtt(app)
except:
    logging.error("Can't connect to MQTT Broker")