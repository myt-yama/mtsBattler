from bottle import route, run, default_app, template

@route('/battler')
def battler():
    return 'battler success!!'

@route('/battler/sample')
def sample():
    title='Hello world'
    return template('sample', title=title)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=True, reloader=True)
else:
    application = default_app()
