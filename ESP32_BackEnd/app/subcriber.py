
from app import mqtt
import logging
from app import db
from .parse import parse_body_data
from app.models import ReadDataSensorTable
from app.vntime import *
from datetime import datetime
from write_log import setup_logger

count = 0
sensorData = {}
mqtt.subscribe("ESP32/SendQT")

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    pass

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
	logging.warning("on message")
	global count
	rawData = message.payload.decode('utf-8')
	payload = parse_body_data(rawData)
	logging.warning(f"Receive data {payload}")

	if type(payload) is dict:
		for x in payload:
			if x == "Temp":
				count = count + 1
				temp = payload['Temp']
				if temp == "nan":
					temp = 0
			if x == "Humi":
				humi = payload['Humi']
				if humi == "nan":
					humi = 0
			if x == "Mq2":
				mq2 = payload['Mq2']
				if mq2 == "nan":
					mq2 = 0
	
	if count == 6:
		now = datetime.now()
		timeStamp = now.timestamp()
		timeNow = VnTimestamp.get_date_time_str(timeStamp)
		count = 0
		insertData = ReadDataSensorTable(temp = temp, humi = humi, mq2 = mq2, createAt = timeNow)
		print("Insert into database")
		db.session.add(insertData)
		db.session.commit()

		readSensors = ReadDataSensorTable.query.order_by(ReadDataSensorTable.id.desc()).first()
		readSensorDict = readSensors.__dict__
		readSensorDict.pop("_sa_instance_state")

		setup_logger(name = 'log', log_file= 'logs/log.txt', message= readSensorDict)

		 


