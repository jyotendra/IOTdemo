"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from tobluemix import app
import paho.mqtt.client as mqtt
import mypaho



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        led_state = None
    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )

@app.route('/getstate', methods=['GET','POST'])
def getstate():
    client = mqtt.Client()
    client.on_connect = mypaho.on_connect
    client.on_message = mypaho.on_message
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()

    mypaho.set_topic(mypaho.send_topic)
    client.subscribe(mypaho.current_topic)

    mypaho.set_topic(mypaho.request_topic)
    client.publish(mypaho.current_topic)
    
    return render_template('index.html',led_state = str(mypaho.current_msg))




