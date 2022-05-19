
import logging

from app import api
from flask_restful import Resource, Api, request
from app import mqtt
from app.models import ReadDataSensorTable
from write_log import setup_logger
from app.subcriber import sensorData

class EspControlApi(Resource):
	def get(self):
		global ledState
		readSensors = ReadDataSensorTable.query.order_by(ReadDataSensorTable.id.desc()).first()
		readSensorDict = readSensors.__dict__
		readSensorDict.pop("_sa_instance_state")
		return readSensorDict

	def post(self):
		logging.warning("on message")
		data = request.get_json(force=True) 
		logging.error(data)
		mqtt.publish("hethongnhung/control", f"{data['led']} {data['relay']}")

		return "DONE!"


api.add_resource(
	EspControlApi,
	"/control"
)
