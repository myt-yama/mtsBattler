from controllers.controller import *
from models.monster import Monster

app: Bottle = Bottle()

@app.route('/index')
@app.route('/result')
def index():
    """
    初期画面表示

    Returns
    ----------
    templateオブジェクト
    """
    return template('summon_index')

@app.route('/result', 'POST')
def battle():
    """
    モンスター同士の攻撃処理
    　処理結果を画面に返す

    Returns
    ----------
    templateオブジェクト
    """
    monster_params = {
        'team': 'team-A',
        'name': request.forms.getunicode('name')
    }
    summoned_monster = Monster(monster_params, True)
    params = {
        'name': summoned_monster.get_name(),
        'hp' : summoned_monster.get_hp(),
        'power' : summoned_monster.get_power(),
        'defence': summoned_monster.get_defence(),
        'attribute': summoned_monster.get_attribute(),
    }
    return template('summon_result', params=params)
