"""
This script runs the FlaskWebProject1 application using a development server.
"""

import os
from tobluemix import app

port = os.getenv('PORT', '5000')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=int(port))
