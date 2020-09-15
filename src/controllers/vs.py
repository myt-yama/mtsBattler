from controllers.controller import *
from models.monster import Monster
from models import redismodel

app: Bottle = Bottle()

#


class VsController(Controller):
    def __init__(self):
        super().__init__(__file__)


controller = VsController()


@app.route('/')
def index():
    return controller.template('index')
