from bottle import jinja2_template as template
from bottle import route, Bottle, request
import redis

app: Bottle = Bottle()

@app.route('/index')
def index():
    sr = redis.Redis(host='redis', port=6379, db=0)
    sr.set("test-key", "テストバリュー")
    return sr.get("test-key").decode()
