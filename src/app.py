from bottle import route, run, default_app

@route('/test')
def test():
    return 'test success'
if __name__ == '__main__':
    run(host='0.0.0.0', port=3031, debug=True, reloader=True)
else:
    application = default_app()
