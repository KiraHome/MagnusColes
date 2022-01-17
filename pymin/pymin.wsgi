#!/usr/bin/python3.8

import logging, sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/pymin')
from pymin import create_app
application = create_app()



