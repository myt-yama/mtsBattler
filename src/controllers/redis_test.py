from bottle import jinja2_template as template
from bottle import route, Bottle, request
from utils.dbaccess import DbAccess

import logging
logging.basicConfig(level=logging.DEBUG)

app: Bottle = Bottle()

@app.route('/index')
@app.route('/register_team')
def index():
    return template('redis_index')

@app.route('/register_team', 'POST')
def register_team():
    team_name = request.forms.getunicode('team_name')
    r = DbAccess.get_connection_to_redis()
    r.sadd('teams', team_name)
    return template('redis_index')

@app.route('/monsters')
@app.route('/monsters', 'POST')
def monsters():
    r = DbAccess.get_connection_to_redis()
    if request.method == 'POST':
        team_name = request.forms.getunicode('team')
        monsters_db = list(r.smembers(team_name+'monster'))
        monsters = []
        for monster in monsters_db:
            status = r.hgetall(monster)
            status['attribute'] = ''.join(list(map(lambda x: convert_attribute_cd(x), status['attribute'].split(','))))
            monsters.append(status)
    else:
        monsters = ''
    teams =list(r.smembers('teams'))
    params = {
         'teams': teams,
         'monsters': monsters,
    }
    return template('redis_monsters', params=params)

@app.route('/register_monster', 'POST')
def register_monster():
    team_name = str(request.forms.getunicode('team-name'))
    name = str(request.forms.getunicode('name'))
    hp = request.forms.getunicode('hp')
    power = request.forms.getunicode('power')
    defence = request.forms.getunicode('defence')
    attribute = request.forms.getunicode('attribute')

    r = DbAccess.get_connection_to_redis()
    p = r.pipeline()
    p.sadd(team_name+'monster', team_name+'-'+name)
    p.hset(team_name+'-'+name, 'name', name)
    p.hset(team_name+'-'+name, 'hp', hp)
    p.hset(team_name+'-'+name, 'power', power)
    p.hset(team_name+'-'+name, 'defence', defence)
    p.hset(team_name+'-'+name, 'attribute', attribute)
    p.execute()

    teams =list(r.smembers('teams'))
    params = {
         'teams': teams,
         'monsters': '',
    }
    return template('redis_monsters', params=params)

def convert_attribute_cd(attribute_cd):
    if attribute_cd == '1':
        return '火'
    elif attribute_cd == '2':
        return '水'
    return '土'


