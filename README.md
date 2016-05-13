# IOTdemo
This is setup for IOT demo using IBM bluemix as cloud platform.

The project connects an LED and a photoresistor sensor to IBM Bluemix cloud. The idea used in this project can be 
extended to interface other outputs (using relays) or multiple sensors. Following platforms are used for entire development.

=========
Hardware:
=========

1. Raspberry pi : for interfacing sensor and LED.
2. MCP3008 : An ADC, as Raspberry pi don't have its own. It comes with 8 channels, so at a time it can connect to 8 devices.
3. Photoresistor sensor: To detect variation in light intensity.
4. LED

=============
Software:
=============

1. Paho: This is a MQTT client library to help connect to broker (Mosquitto in our case).
2. Flot: Its a javascripit library to generate graphs.
3. Flask: Its a web-framework for python.
4. IBM Bluemix: Used as cloud platform.

This project requires fair knowledge of :

HTML, Javascript, AJAX, JQuery and CSS.

However, as everything is held together by python - good python knowledge is required to understand the project.

================================================
######## Detailed Project Description ##########
================================================

This is a demo project for "Internet of Things" (IOT). In this demo project we will try to connect led and a sensor to 
IBM bluemix cloud, so that LED can be operated through any smartphone/ tablet/ pc etc. Likewise, sensor data will be
furnished to device requesting it.

We will be using MQTT protocol for overall communication. In MQTT protocol, clients connect to each other via a central 
broker. "Mosquitto" is used as public broker in this project. The raspberry-pi, which interfaces the LED and sensor uses 
"MQTT-Paho" library (written in python), to connect to the broker.

On invoking the Paho script alongwith RPi.GPIO ,to perform I/O operation, raspberry pi sits to receive any command on 
subscribed topic. As a certain message is received on some topic - either LED is toggled or sensor data is published.



========================
***** Blog Entry *******
========================

I will try to explain entire project, in chunks - one at a time, on 

https://jyotendrasharmaprojects.wordpress.com/category/iot/

Find posts by name of "IOT Demo - Part #"









