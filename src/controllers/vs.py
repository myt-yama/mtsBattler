from controllers.controller import *
from models.monster import Monster
from facades.vsfacade import VsFacade
from facades.battlefacade import BattleFacade

app: Bottle = Bottle()


class VsController(Controller):
    def __init__(self):
        super().__init__(__file__)


controller = VsController()


@app.route('/')
def index():
    return controller.template('index')


@app.route('/battle')
@app.route('/battle', 'POST')
def battle():
    """
    戦闘画面
    """
    battle_id = request.forms.getunicode('battle_id')
    # logging.info(battle_id)

    if battle_id is None:
        monster_ids = [
            'team-A-jiro',
            'team-A-mini'
        ]

        battle_facade = BattleFacade()
        battle = battle_facade.ready(monster_ids)
    else:
        commands = {
            'P1': request.forms.get('battle_command_P1'),
            'P2': request.forms.get('battle_command_P2'),
        }

        battle_facade = BattleFacade(battle_id)
        battle = battle_facade.fight(commands)

    return controller.template('battle', battle=battle)
