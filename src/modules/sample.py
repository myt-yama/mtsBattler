from bottle import jinja2_template as template
from bottle import route, Bottle, request
from models import monster

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
    monster_a = monster.Monster(100, 10)
    monster_b = monster.Monster(110, 20)
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
    monster_a = monster.Monster(int(request.forms.get('a_hp')), 10)
    monster_b = monster.Monster(int(request.forms.get('b_hp')), 20)

    monster_a.atack(monster_b)
    monster_b.atack(monster_a)
    params = {
        'title': 'Battle!',
        'a_hp' : monster_a.get_hp(),
        'b_hp' : monster_b.get_hp(),
    }
    return template('sample', params=params)

