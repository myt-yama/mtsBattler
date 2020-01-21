from controllers.controller import *
from models.battle import Battle
from models import redismodel

app: Bottle = Bottle()

@app.route('/')
def index():
    """
    戦闘画面
    """
    battle_status = {}
    battle_status['P1_team'] = 'team-A'
    battle_status['P1_name'] = 'Jiro'
    battle_status['P1_hp'] = 10
    battle_status['P1_attribute_cd'] = '0,2'
    battle_status['P1_attribute'] = '水草'
    battle_status['P1_charge'] = 0
    battle_status['P2_team'] = 'team-B'
    battle_status['P2_name'] = 'Taro'
    battle_status['P2_hp'] = 10
    battle_status['P2_attribute_cd'] = '1'
    battle_status['P2_attribute'] = '火'
    battle_status['P2_charge'] = 0

    battle = Battle()
    battle.set_battle(battle_status)
    battle.register()

    return template('fight_index', battle=battle)

@app.route('/battle', 'POST')
def battle():
    """
    バトルコマンド実行
    """

    battle_id = request.forms.getunicode('battle_id')
    battle_commands = request.forms.getunicode('battle_commands')

    battle = Battle(battle_id, battle_commands)
    battle.select()

    # TODO: バトルロジック作成
    battle.fight()
    battle.P1_hp = 20

    return template('fight_index', battle=battle)
