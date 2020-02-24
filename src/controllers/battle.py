from controllers.controller import *
from models.monster import Monster
from models import redismodel

app: Bottle = Bottle()

#

@app.route('/')
def index():
    """
    対戦前ページ

    Returns
    ----------
    templateオブジェクト
    """

    teams = redismodel.RedisTeams().select()
    return template('vs', teams = teams)

# @app.route('/choose')
# def choose():
#     """
#     対戦キャラ選択ページ

#     Returns
#     ----------
#     templateオブジェクト
#     """
#     team = 'A'
#     monsters = redismodel.RedisMonster().select_all(team)

#     return template('choose', monsters=monsters)

@app.route('/', 'post')
def post():
    """
    対戦キャラ選択ページ

    Returns
    ----------
    templateオブジェクト
    """

    # ajaxで渡ってきたteamを受け取り表示に渡す
    team = request.forms.getunicode('team')
    logging.info(team)
    monsters = redismodel.RedisMonster().select_all(team)

    return template('choose', monsters=monsters)

@app.route('/register', 'post')
def register():
    """
    バトルに使うキャラの決定
    """
    id = request.forms.getunicode('id')
    # logging.info(target)
    monster = redismodel.RedisMonster().select(id)
    monster = {
        'team' : monster.get_team()
        , 'name' : monster.get_name()
    }

    return monster