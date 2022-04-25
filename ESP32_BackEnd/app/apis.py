import imp
import logging
from app import api
from flask_restful import Resource, Api, request
from app import mqtt
from app.models import ReadDataSensorTable
from write_log import setup_logger
from app.subcriber import sensorData

class TestApi(Resource):
	def get(self):
		global ledState
		readSensors = ReadDataSensorTable.query.order_by(ReadDataSensorTable.id.desc()).first()
		readSensorDict = readSensors.__dict__
		readSensorDict.pop("_sa_instance_state")
		return readSensorDict

	def post(self):
		data = request.get_json(force=True) 
		logging.warning(data)

		print(data)
		if data['led'] == 1:
			mqtt.publish("MQTT/SendQT", "LEDON")
			setup_logger(name = 'log', log_file= 'logs/log.txt', message= "LEDON")
	
		if data['led'] == 0:
			mqtt.publish("MQTT/SendQT", "LEDOFF")
			setup_logger(name = 'log', log_file= 'logs/log.txt', message= "LEDOFF")
		



# class DownloadFileLogApi(Resource):
#     def get(self):
#         pass
api.add_resource(
	TestApi,
	"/test"
)
