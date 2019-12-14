from bottle import jinja2_template as template
from bottle import route, Bottle, request
import redis
import pickle

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
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    r.sadd('teams', team_name)
    return template('redis_index')

@app.route('/monsters')
@app.route('/monsters', 'POST')
def monsters():
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    if request.method == 'POST':
        team_name = request.forms.getunicode('team')
        r = redis.StrictRedis(host='redis', port=6379, db=0)
        monsters_db = list(map(lambda x: x.decode(), list(r.smembers(team_name+'monster'))))
        monsters = []
        for monster in monsters_db:
            status = {}
            for k, v in r.hgetall(monster).items():
                status[k.decode()] = v.decode()
            # logging.info(status['attribute'].split(','))
            status['attribute'] = ''.join(list(map(lambda x: convert_attribute_cd(x), status['attribute'].split(','))))
            monsters.append(status)
    else:
        monsters = ''
    teams = list(map(lambda x: x.decode(), list(r.smembers('teams'))))
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

    r = redis.StrictRedis(host='redis', port=6379, db=0)
    p = r.pipeline()
    p.sadd(team_name+'monster', team_name+'-'+name)
    p.hset(team_name+'-'+name, 'name', name)
    p.hset(team_name+'-'+name, 'hp', hp)
    p.hset(team_name+'-'+name, 'power', power)
    p.hset(team_name+'-'+name, 'defence', defence)
    p.hset(team_name+'-'+name, 'attribute', attribute)
    p.execute()

    teams = list(map(lambda x: x.decode(), list(r.smembers('teams'))))
    params = {
         'teams': teams,
         'monsters': '',
    }
    return template('redis_monsters', params=params)

def convert_attribute_cd(attribute_cd):
    # logging.info(attribute_cd)
    if attribute_cd == '1':
        return '火'
    elif attribute_cd == '2':
        return '水'
    return '土'


