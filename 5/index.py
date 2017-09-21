from bottle import Bottle, request, template
list_of_name = ["name", "address", "email", "tele", 'size', 'topping']
price = {'9': 1000, '12': 1500, '18': 2000}
app = Bottle()
HOST = 'localhost'
PORT = 81
def dicto_test(dict):
    try:
        x = dict['nr']
        return True
    except KeyError:
        return False

@app.error(500)
def error500(error):
    return '500 Error'


@app.get('/')
def index():
    return template('index.tpl')


@app.post('/')
def index_processing():
    info = {x: request.forms.get(x) for x in list_of_name}
    x = ['y' for x in range(0, 3) if request.forms.get('topping[{}]'.format(x)) is not None]
    info['topping'] = ', '.join([request.forms.get('topping[{}]'.format(x)) for x in range(0, len(x)) if len(str(request.forms.get('topping[{}]'.format(x)))) > 0])
    print(info['topping'])
    info['price'] = price[info['size']] if len(info['topping']) < 2 else price[info['size']] + len(info['topping'].split(' ')) * 200
    info['vsk'] = int(info['price'] * 0.25)
    info['nr'] = info['nr'] + 1 if dicto_test(info) else 1
    return template('results.tpl', info)

app.run(host=HOST, port=PORT)
