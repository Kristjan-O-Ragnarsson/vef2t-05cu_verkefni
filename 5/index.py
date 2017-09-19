from bottle import Bottle, request, error, template
list_of_name = ["name", "address", "email", "tele", 'size', 'topping']
price = {'9': 1000, '12': 1500, '18': 2000}
app = Bottle()
HOST = 'localhost'
PORT = 81


@app.error(500)
def error500(error):
    return '500 Error'


@app.get('/')
def index():
    return template('index.tpl')


@app.post('/')
def index_processing():
    info = {x: request.forms.get(x) for x in list_of_name}
    info['topping'] = ' '.join([request.forms.get('topping[{}]'.format(x)) for x in range(0, 3) if len(str(request.forms.get('topping[{}]'.format(x)))) > 0])
    info['price'] = price[info['size']] + len(info['topping'].split(' ')) * 200
    return template('results.tpl', info)

app.run(host=HOST, port=PORT)
