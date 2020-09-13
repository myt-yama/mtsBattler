from controllers.controller import *
from models.monster import Monster
from facades.battlefacade import BattleFacade

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

        battle_facade = BattleFacade()
        battle = battle_facade.ready(monsters)

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

        battle_facade = BattleFacade(battle_id)
        battle = battle_facade.fight(commands)
        # logging.info(battle.commands)

        return template('fight_index', battle=battle)
