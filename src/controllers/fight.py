from controllers.controller import *
from models.battle import Battle
from models.monster import Monster
from models import redismodel

app: Bottle = Bottle()

class FightController(Controller):
    @app.route('/')
    def index():
        """
        戦闘画面
        """
        monsters = [
            Monster({'name': 'Jiro', 'team': 'team-A'}, True),
            Monster({'name': 'Taro', 'team': 'team-B'}, True),
        ]

        battle = Battle()
        battle.set_monsters(monsters)
        battle.register()

        return template('fight_index', battle=battle)

    @app.route('/battle', 'POST')
    def battle():
        """
        バトルコマンド実行
        """

        battle_id = request.forms.getunicode('battle_id')
        commands = {
            'P1' : request.forms.get('battle_command_P1'),
            'P2' : request.forms.get('battle_command_P2'),
        }

        battle = Battle(battle_id)
        battle.select()

        # TODO: バトルロジック作成
        battle.set_command(commands)
        battle.fight()
        # logging.info(battle.commands)

        return template('fight_index', battle=battle)
