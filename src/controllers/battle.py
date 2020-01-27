from controllers.controller import *
from models.monster import Monster
from models import redismodel

app: Bottle = Bottle()

#

@app.route('/')
def index():
    """
    モンスター生成画面表示

    Returns
    ----------
    templateオブジェクト
    """
    return template('vs')
