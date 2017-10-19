"""
Kristjan O.
"""
import bottle
import json
import urllib.request
api = {'consert': 'http://apis.is/concerts'}


def get_api_data(api_):
    with urllib.request.urlopen(api_) as dump:
        data = json.loads(dump.read().decode())
    return data


@bottle.route('/')
def index():
    info = get_api_data(api['consert'])
    for i in info['results']:
        v = i['dateOfShow'].split('T')
        i['dateOfShow'] = ' '.join((v[1], '-'.join(v[0].split('-')[::-1])))
    return bottle.template('consert.tpl', info)

bottle.run(
    host='localhost',
    port=81
)
