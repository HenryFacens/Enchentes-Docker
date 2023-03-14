import paho.mqtt.client as mqtt
import apiPI

# MQTT broker settings
MQTT_BROKER_HOST = "34.234.193.23"
MQTT_BROKER_PORT = 1883
# MQTT_USERNAME = "your-username"
# MQTT_PASSWORD = "your-password"
MQTT_TOPIC = "/smart/lago/nivel"

# MQTT client instance
client = mqtt.Client()

# Callback function when connected to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Failed to connect to MQTT broker")

# Callback function when receiving a message from the MQTT broker
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")
    req = message.payload.decode()
    ptM_Dist = apiPI.getPiPoints('tcc_distancia')[0]
    print(apiPI.setValue(ptM_Dist['WebId'], req))



# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
# client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

# Start the MQTT client loop to receive messages
client.loop_forever()
