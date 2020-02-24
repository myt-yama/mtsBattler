from bottle import route, run, static_file, Bottle
from bottle import jinja2_template as template
from controllers import  farm, fight, battle

main: Bottle = Bottle()

@main.route('/static/<filePath:path>')
def static(filePath):
    return static_file(filePath, root='./static')

@main.route('/battler')
def battler():
    return template('battler')


# 以下、URLに対応する別々のモジュールを呼ぶ
main.mount('/battler/farm', farm.app)
main.mount('/battler/fight', fight.app)
main.mount('/battler/battle', battle.app)


if __name__ == '__main__':
    # 開発用アプリ起動
    main.run(host='0.0.0.0', port=8000, debug=True, reloader=True)
else:
    # Nginx経由でアプリ起動
    application = main
