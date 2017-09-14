from bottle import Bottle, request, template, static_file, HTTPError

app = Bottle()
links = [('', 'Home'), ('?page=0', 'Frétt 1'), ('?page=1', 'Frétt 2'), ('?page=2', 'Frétt 3'),
         ('?page=4', 'linkur sem virkar ekki')]

err = {404: {'code': '404', 'joke': 'What are you doing here'}}

news = [{'title': 'þessi snígil vann heimsmetið', 'author': 'gus@tskoli.is',
  'content': 'Þessi snígil vann heimsmetið í að hoppa ', 'links': links, 'img': '600.jpg', 'p': '?page=0'},
 {'title': 'þessi snígil vann heimsmetið', 'author': 'gus@tskoli.is',
  'content': 'Þessi snígil vann heimsmetið í að hoppa ', 'links': links, 'p': '?page=0'},
{'title': 'þessi snígil vann heimsmetið', 'author': 'gus@tskoli.is',
  'content': 'Þessi snígil vann heimsmetið í að hoppa ', 'links': links, 'p': '?page=0'}
 ]
home = {'title': 'Frétta síðan mikla',
        'content': 'Hin mikkla fræga mikilvæga frétta síða',
        'ne': [{'title': x['title'], 'author': x['author'], 'content': x['content'], 'p': x['p']} for x in news],
        'links': links}

@app.error(404)
def error404(error):
    return template('error.tpl', err[404])


@app.route('/')
def index():
    page = request.query.page
    try:
        if page.isdigit():
            return template('new.tpl', news[int(page)])
        else:
            print(home['ne'])
            return template('index', home)
    except IndexError:
        raise HTTPError(404)


@app.get('/static/img/<path:re:.*\.(png|jpg)>')
def img(path):
    return static_file(path, root='./img')


@app.get('/static/css/<path:re:.*\.css>')
def css(path):
    return static_file(path, root='./css')

app.run(host='localhost', port=81)