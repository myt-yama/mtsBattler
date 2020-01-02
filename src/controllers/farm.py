from controllers.controller import *
from models.monster import Monster
from models import redismodel

app: Bottle = Bottle()

@app.route('/')
@app.route('/summon')
def index():
    """
    モンスター生成

    Returns
    ----------
    templateオブジェクト
    """
    teams = redismodel.RedisTeams().select()
    return template('farm_summon', teams=teams)

@app.route('/summon', 'POST')
def summon_post():
    monster_params = {
        'name' : request.forms.getunicode('name'),
        'team' : request.forms.getunicode('team'),
    }
    monster = Monster(monster_params, True)
    redismodel.RedisMonster().register(monster)

    return template('status',params=monster)
