import bottle
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)


@bottle.route('/')
def index():
    session = bottle.request.environ.get('beaker.session')
    session['cart'] = 1 if session.get('cart') is None else session.get('cart') + 1
    return 'ég tok bara nuna eftir að ég átti að gera teljara henti þessu saman á 5 min {}'.format(session.get('cart'))

bottle.run(
    app=app,
    host='localhost',
    port=81
)
