from bottle import route, run, static_file, Bottle
from bottle import jinja2_template as template
from modules import sample

main: Bottle = Bottle()

@main.route('/static/<filePath:path>')
def static(filePath):
    return static_file(filePath, root='./static')

main.mount('/battler/sample', sample.app)

# @route('/battler')
# def battler():
#     return 'battler success!!'

if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8000, debug=True, reloader=True)
else:
    application = main
