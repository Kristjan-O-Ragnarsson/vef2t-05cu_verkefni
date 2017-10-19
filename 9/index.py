"""
Kristjan O.
"""
import bottle
import json

bace = {'myndir': ['370x256', '369x257', '368x258'], 'head': 'Myndir sem eru valdar fo einhverjum'}
WRITE = 'w'
READ = 'r'
FILE_NAME = 'info.json'
ENCODING = 'utf-8'


def read_json(file):
    with open(file, READ, encoding=ENCODING) as json_data:
        dump = json.load(json_data)
    return dump


def write_json(file, _input):
    with open(file, WRITE, encoding=ENCODING) as json_file:
        json.dump(_input, json_file)

#write_json(FILE_NAME, bace)

info = read_json(FILE_NAME)


@bottle.route('/')
def index():
    return bottle.template('images.tpl', info)


@bottle.get('/img/<path:re:.*\.(png|jpg)>')
def img(path):
    return bottle.static_file(path, root='./static')


@bottle.get('/modify')
def add_pic():
    return bottle.template('add.tpl')


@bottle.post('/modify')
def proc_pic_add():
    keys = [x for x in bottle.request.forms]
    formd = [bottle.request.forms.get(x) for x in keys]
    for it in formd:
        info['myndir'].append(it)
    write_json(FILE_NAME, info)
    return bottle.redirect('/')


bottle.run(
    host='localhost',
    port=81
)