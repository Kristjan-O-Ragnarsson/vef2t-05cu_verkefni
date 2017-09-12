from bottle import Bottle, request, template, static_file, HTTPError

app = Bottle()

err = {404: {'code': '404', 'joke': 'What are you doing here'}}


@app.error(404)
def error404(error):
    return template('error.tpl', err[404])


@app.route('/')
def index():
    return


@app.get('/static/img/<path:re:.*\.(png|jpg)>')
def img(path):
    return static_file(path, root='./img')


@app.get('/static/css/<path:re:.*\.css>')
def css(path):
    return static_file(path, root='./css')

app.run(host='localhost', port=81)