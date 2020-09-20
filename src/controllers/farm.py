from controllers.controller import *
from facades.farmfacade import FarmFacade
from facades.summonfacade import SummonFacade

app: Bottle = Bottle()


class FarmController(Controller):
    def __init__(self):
        super().__init__(__file__)


controller = FarmController()

confirm_buttons = {
    'cancel': '0',
    'register': '1',
}


@app.route('/')
def index():
    """
    モンスター管理画面表示
    """
    team = 'team-A'
    farm_facade = FarmFacade()
    monsters = farm_facade.fetch_monsters(team)
    logging.info(monsters)
    return controller.template('index', monsters=monsters, button_message='ばいばい')


@app.route('/summon')
def summon():
    """
    モンスター生成画面表示

    Returns
    ----------
    templateオブジェクト
    """
    summon_facade = SummonFacade()
    teams = summon_facade.fetch_teams()
    return controller.template('summon', teams=teams)


@app.route('/summon', 'POST')
def summon_post():
    """
    モンスター登録確認画面表示
        モンスターの仮登録も行う

    Returns
    ----------
    templateオブジェクト
    """
    name = request.forms.getunicode('name')
    team = request.forms.getunicode('team')

    summon_facade = SummonFacade()
    monster = summon_facade.summon(team, name)
    params = {
        'monster': monster,
        'confirm_buttons': confirm_buttons,
    }

    return controller.template('status', params=params)


@app.route('/register', 'POST')
def register():
    """
    モンスター登録処理
        本登録 or キャンセル（仮登録データ削除）
    """

    id = request.forms.getunicode('id')
    register_flg = request.forms.getunicode('register_flg')

    logging.info(register_flg)
    summon_facade = SummonFacade(id)
    if register_flg == confirm_buttons['register']:
        # 登録
        logging.info('regist')
        summon_facade.register()
    else:
        # キャンセル
        logging.info('cancel')
        summon_facade.register_cancel()


# TODO: 修正
@app.route('/delete', 'POST')
def delete():
    """
    モンスター削除処理
    """
    id = request.forms.getunicode('key')
    team = request.forms.getunicode('team')

    summon_facade = SummonFacade()
    summon_facade.delete(id, team)

    farm_facade = FarmFacade()
    monsters = farm_facade.fetch_monsters(team)
    return controller.template('monster', monsters=monsters)
