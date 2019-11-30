from bottle import jinja2_template as template
from bottle import route, Bottle, request

app: Bottle = Bottle()

@app.route('/index')
def index():
    params = {
        'title': 'Index',
        'a_hp' : '',
        'b_hp' : '',
    }
    return template('sample', params=params)

@app.route('/battle', 'POST')
def battle():
    params = {
        'title': 'Battle!',
        'a_hp' : request.forms.get('a_hp'),
        'b_hp' : request.forms.get('b_hp'),
    }
    return template('sample', params=params)

