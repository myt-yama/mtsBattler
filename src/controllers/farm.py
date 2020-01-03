from controllers.controller import *
from models.monster import Monster
from models import redismodel

app: Bottle = Bottle()

# 
confirm_buttons = {
    'cancel' : '0',
    'register' : '1',
}

@app.route('/')
@app.route('/summon')
def index():
    """
    モンスター生成画面表示

    Returns
    ----------
    templateオブジェクト
    """
    teams = redismodel.RedisTeams().select()
    return template('farm_summon', teams=teams)

@app.route('/summon', 'POST')
def summon_post():
    """
    モンスター登録確認画面表示
        モンスターの仮登録も行う

    Returns
    ----------
    templateオブジェクト
    """
    monster_params = {
        'name' : request.forms.getunicode('name'),
        'team' : request.forms.getunicode('team'),
    }

    monster = Monster(monster_params, True)
    redismodel.RedisMonster().register(monster, True)
    params = {
        'monster' : monster,
        'confirm_buttons' : confirm_buttons,
    }

    return template('status',params=params)

@app.route('/register', 'POST')
def register():
    """
    モンスター登録処理
        本登録 or キャンセル（仮登録データ削除）
    """
    id = request.forms.getunicode('id')
    register_flg = request.forms.getunicode('register_flg')
    if register_flg == confirm_buttons['register']:
        # 登録
        monster = redismodel.RedisMonster().select('tmp-'+id)
        redismodel.RedisMonster().delete('tmp-'+id)
        redismodel.RedisMonster().register(monster)
    else:
        # キャンセル
        redismodel.RedisMonster().delete('tmp-'+id)
