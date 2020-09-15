from controllers.controller import *
from models.monster import Monster
from facades.battlefacade import BattleFacade

app: Bottle = Bottle()


class BattleController(Controller):
    def __init__(self):
        super().__init__(__file__)


controller = BattleController()


@app.route('/')
def index():
    return controller.template('index')


@app.route('/fight')
@app.route('/fight', 'POST')
def battle():
    """
    戦闘画面
    """
    battle_id = request.forms.getunicode('battle_id')
    logging.info(battle_id)

    if battle_id is None:
        monsters = [
            Monster({'name': 'Jiro', 'team': 'team-A'}, True),
            Monster({'name': 'Taro', 'team': 'team-B'}, True),
        ]

        battle_facade = BattleFacade()
        battle = battle_facade.ready(monsters)
    else:
        commands = {
            'P1': request.forms.get('battle_command_P1'),
            'P2': request.forms.get('battle_command_P2'),
        }

        battle_facade = BattleFacade(battle_id)
        battle = battle_facade.fight(commands)

    return controller.template('battle', battle=battle)


# @app.route('/battle/fight', 'POST')
# def battle():
#     """
#     バトルコマンド実行
#     """

#     battle_id = request.forms.getunicode('battle_id')
#     # logging.info(battle.commands)

#     return controller.template('index', battle=battle)
