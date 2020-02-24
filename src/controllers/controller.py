from bottle import jinja2_template as template
from bottle import route, Bottle, request
import os

import logging
logging.basicConfig(level=logging.DEBUG)

class Controller:
    def __init__(self, file_obj):
        self.module = os.path.splitext(os.path.basename(file_obj))[0]+'/' 

    def template(self, filename, **kargs):
        # logging.info(kargs)
        return template(self.module+filename, **kargs)
