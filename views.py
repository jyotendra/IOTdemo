"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from tobluemix import app
import mypaho

led_state = None

def setLedState(inp):
    global led_state
    On = ("on", "On", "ON", 1, "1")
    Off = ("off","Off","OFF", 0, "0")
    if (inp in Off):
        led_state = "Off"
                        
    elif (inp  in On):
        led_state = "On"

@app.route('/')
@app.route('/index.html')
def home():
    global led_state
    """Renders the home page."""
    mypaho.client.subscribe(mypaho.send_topic)
    mypaho.client.publish(mypaho.request_topic)
    setLedState(mypaho.retCurrentMsg())
    return render_template(
        'index.html',
        led_state = led_state
    )

@app.route('/sensor.html')
def sensor():
    mypaho.client.subscribe(mypaho.sensor_data_topic)
    """Renders the sensor page."""
    return render_template(
        'sensor.html'
    )

@app.route('/sensordata')
def sensordata():
    """Get sensor data"""
    mypaho.client.publish(mypaho.sense_topic)
    return mypaho.current_msg
    

@app.route('/setstate', methods=['GET','POST'])
def setstate():
    global led_state
    if led_state == "Off":
        mypaho.client.publish(mypaho.cmd_topic,"On")
        setLedState("1")
    elif led_state == "On":
        mypaho.client.publish(mypaho.cmd_topic,"Off")
        setLedState("0")
    return render_template(
    'index.html',
    led_state = led_state)




