from controllers.controller import *
from models import redismodel, monster2

app: Bottle = Bottle()

@app.route('/index')
@app.route('/register_team')
def index():
    return template('redis_index')

@app.route('/register_team', 'POST')
def register_team():
    team_name = request.forms.getunicode('team_name')
    redismodel.RedisTeams().register(team_name)
    return template('redis_index')

@app.route('/monsters')
@app.route('/monsters', 'POST')
def monsters():
    if request.method == 'POST':
        team = request.forms.getunicode('team')
        monsters = redismodel.RedisMonster().select_all(team)
    else:
        monsters = ''
    teams = redismodel.RedisTeams().select()
    params = {
         'teams': teams,
         'monsters': monsters,
    }
    return template('redis_monsters', params=params)

@app.route('/register_monster', 'POST')
def register_monster():
    team = str(request.forms.getunicode('team-name'))
    name = str(request.forms.getunicode('name'))
    monster_params = {
        'name' : name,
        'team' : team,
    }
    monster = monster2.Monster(monster_params, True)
    redismodel.RedisMonster().register(monster)

    teams = redismodel.RedisTeams().select()
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


