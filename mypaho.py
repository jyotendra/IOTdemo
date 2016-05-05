""" This module will contain topics and callback handlers """


request_topic = "js/object/request/status"
# when a ping on this topic is received, led status is sent on "send_topic"

send_topic = "js/object/send/status"

#one need to subscribe to this topic to get status of led.
#Remember to first request on "request_topic" to successfully get message back on the topic.

cmd_topic  = "js/object/command"
# This topic is used to give On or Off command.

current_topic = None # This topic will hold the current topic according to the context
current_msg = "Off" # This global will take in the current message

def set_topic(topic):
    global current_topic 
    current_topic = str(topic)

def on_connect(client, userdata, rc):
    global current_topic
    print("Connected with result code "+str(rc))
    client.subscribe(current_topic)

def on_message(client, userdata, msg):
    global current_msg
    if (msg.topic == send_topic):
        current_msg = str(msg.payload)
        print "LED returned this status: "+str(current_msg)

