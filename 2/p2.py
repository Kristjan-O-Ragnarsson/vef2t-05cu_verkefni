from bottle import Bottle
HOST = 'localhost'
PORT = 81

app = Bottle()


@app.route('/hello')
def hello():
    return 'Halló Heimur'

app.run(host=HOST, port=PORT)
