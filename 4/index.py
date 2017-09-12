from bottle import Bottle, request, template, static_file, HTTPError

app = Bottle()

err = {404: {'code': '404', 'joke': 'What are you doing here'}}

links = [('', 'Home'), ('?p=1', 'Steve Jobs'), ('?p=2', 'Pictures'), ('?p=3', 'Biography'),
         ('?p=4', 'linkur sem virkar ekki')]


@app.error(404)
def error404(error):
    return template('error.tpl', err[404])


@app.route('/')
def index():
    data = {0: {'title': 'Home', 'img': 'stevejobs.jpg', 'links': links[1:5]},
            1: {'title': 'Steve', 'img': 'stevejobs.jpg', 'links': links},
            2: {'title': 'Picture', 'img': 'stevejobs.jpg', 'links': links},
            3: {'title': 'Biography', 'img': 'stevejobs.jpg', 'links': links}
            }

    ss = request.query.p
    try:
        return template('main.tpl', data[int(ss)] if (ss.isdigit()) else data[0])
    except KeyError:
        raise HTTPError(404)


@app.get('/static/img/<path:re:.*\.(png|jpg)>')
def img(path):
    return static_file(path, root='./img')


@app.get('/static/css/<path:re:.*\.css>')
def css(path):
    return static_file(path, root='./css')

app.run(host='localhost', port=81)
