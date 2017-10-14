import bottle, random, string
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}

wares = {
    '1': {'item': 'vara1', 'id': '1', 'h': 'Þessi vara1 er ein sú besta frá VeAreTheBigestMoneyGrabbers EHF'},
    '2': {'item': 'vara2', 'id': '2', 'h': 'Þessi vara2 er ein sú besta frá VeAreTheBigestMoneyGrabbers EHF'},
    '3': {'item': 'vara3', 'id': '3', 'h': 'Þessi vara3 er ein sú besta frá VeAreTheBigestMoneyGrabbers EHF'},
    '4': {'item': 'vara4', 'id': '4', 'h': 'Þessi vara4 er ein sú besta frá VeAreTheBigestMoneyGrabbers EHF'},
    '5': {'item': 'vara5', 'id': '5', 'h': 'Þessi vara5 er ein sú besta frá VeAreTheBigestMoneyGrabbers EHF'},
    '6': {'item': 'vara6', 'id': '6', 'h': 'Þessi vara6 er ein sú besta frá VeAreTheBigestMoneyGrabbers EHF'}
         }

app = SessionMiddleware(bottle.app(), session_opts)


@bottle.route('/')
def index():
    return bottle.template('main.tpl', {'title': 'Búð', 'wares': wares})


@bottle.route('/s/<id_>')
def show(id_):
    if id_ in wares.keys():
        return bottle.template('shop.tpl', wares[id_])
    else:
        raise bottle.HTTPError(400, 'Þessi síða er ekki til')


@bottle.route('/buy/<id_>')
def show(id_):
    session = bottle.request.environ.get('beaker.session')
    if id_ in wares.keys():
        session['cart'] = id_ if session.get('cart') is None else session.get('cart') + id_
        print(session['cart'])
        session.save()
        return bottle.redirect('/')
    else:
        raise bottle.HTTPError(400, 'Þessi vara er ekki til')


bottle.run(
    app=app,
    host='localhost',
    port=81
)
