from controllers.controller import *
from models.monster import Monster

app: Bottle = Bottle()

@app.route('/index')
def index():
    """
    初期画面表示

    Returns
    ----------
    templateオブジェクト
    """
    # monster生成
    monster_a = Monster({'name': '轟', 'team': 'team-A'}, True)
    monster_b = Monster({'name': '轆轤', 'team': 'team-B'}, True)
    params = {
        'title': 'Index',
        'a_hp' : monster_a.get_hp(),
        'b_hp' : monster_b.get_hp(),
    }
    return template('sample', params=params)

@app.route('/battle', 'POST')
def battle():
    """
    モンスター同士の攻撃処理
    　処理結果を画面に返す

    Returns
    ----------
    templateオブジェクト
    """
    # monster生成
    a_hp = request.forms.get('a_hp')
    b_hp = request.forms.get('b_hp')
    monster_a = Monster({'name': '轟', 'team': 'team-A', 'hp': a_hp, 'power': 10}, True)
    monster_b = Monster({'name': '轆轤', 'team': 'team-B', 'hp': b_hp, 'power': 20}, True)

    monster_a.atack(monster_b)
    monster_b.atack(monster_a)
    params = {
        'title': 'Battle!',
        'a_hp' : monster_a.get_hp(),
        'b_hp' : monster_b.get_hp(),
    }
    # logging.info(template('sample', params=params))
    return template('sample', params=params)

@app.route('/summon')
def summon():
    """
    モンスター生成

    Returns
    ----------
    templateオブジェクト
    """
    # monster生成
    monster_a = Monster({'name': '轟', 'team': 'team-A'}, True)
    monster_b = Monster({'name': '轆轤', 'team': 'team-B'}, True)
    params = {
        'title': 'Index',
        'a_hp' : monster_a.get_hp(),
        'b_hp' : monster_b.get_hp(),
    }
    return template('summon', params=params)
