class MqttConfigure(object):
    MQTT_BROKER_URL = '13.229.146.39'
    # MQTT_BROKER_URL = '127.0.0.1'
    MQTT_BROKER_PORT = 1883
    # MQTT_USERNAME = 'rostek'
    # MQTT_PASSWORD = '123456'
    MQTT_USERNAME = ''
    MQTT_PASSWORD = ''
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False
    ACTIVE = True
    CA_CERTS = "cert/server.cert"
    FRONTEND_TOPIC = 'agv/realtime'
    FRONTEND_TOPIC_ORDER = 'assy/realtime'
    FRONTEND_CHECK_ORDER = '/test_order'
    FRONTEND_LINE_COUNTING = '/line/assy/frontend'
    AGV_CONTROL = '/agv_flow_control'
    AGV_COUNT_MESSAGE = 20