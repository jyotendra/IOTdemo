""" This module will contain topics and callback handlers """
import paho.mqtt.client as mqtt

request_topic = "js/object/request/status"
# when a ping on this topic is received, led status is sent on "send_topic"

send_topic = "js/object/send/status"

#one need to subscribe to this topic to get status of led.
#Remember to first request on "request_topic" to successfully get message back on the topic.

cmd_topic  = "js/object/command"
# This topic is used to give On or Off command.

sense_topic = "js/object/sense/light"
# At this topic snesor data request will be made

sensor_data_topic = "js/object/sense/light/data"

current_topic = None # This topic will hold the current topic according to the context
current_msg = "Off" # This global will take in the current message


def retCurrentMsg():
    global current_msg
    msg = current_msg
    return str(msg)


#def set_topic(topic):
#    global current_topic 
#    current_topic = str(topic)

def on_connect(client, userdata, rc):
    global current_topic
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    global current_msg
    if (msg.topic == send_topic):
        current_msg = str(msg.payload)
        print "LED returned this status: "+str(current_msg)

    if (msg.topic == sensor_data_topic):
        current_msg = str(msg.payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_start()

