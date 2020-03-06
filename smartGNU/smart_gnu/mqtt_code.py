import paho.mqtt.client as mqtt
from constance import config
# The callback for when the client receives a CONNACK response from the server.

def request_for_publish(topic,pay_load):
    try:
        client = mqtt.Client()
        client.username_pw_set(username=config.MQTT_USERNAME, password=config.MQTT_PASSWORD)
        client.connect(config.MQTT_SERVER, config.MQTT_PUBLIC_PORT, 60)
        client.publish(topic=topic, payload=pay_load, qos=1)
        client.on_publish()
        return
    except Exception as error:
        return error



# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#
#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("home")
#
# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
#
# client.on_connect = on_connect
# client.on_message = on_message
#
#
#
# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()
#
