import bottle
from sys import argv


@bottle.route('/')
def im_online():
    return 'Kristján er búin að vera að nota heroku í dágóðan tíma'

bottle.run(host='0.0.0.0', port=argv[1])