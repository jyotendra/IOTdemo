"""
The flask application package.
"""

from flask import Flask
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#app.debug = True
#Bootstrap(app)
import views