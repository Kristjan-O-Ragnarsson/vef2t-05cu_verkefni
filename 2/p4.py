from bottle import Bottle
HOST = 'localhost'
PORT = 81


three_names = Bottle()


def name_return(id_):
    dictio = {1: 'Gunnar', 2: 'Daníel', 3: 'Þórarinn'}
    try:
        return dictio[id_]
    except KeyError:
        return 'Villa'


@three_names.route('/people/<num:int>')
def name(num):
    return """
               <!DOCTYPE html>
                <html>
                <head>
                    <title></title>
                </head>
                <body>
                    <h1>{}</h1>
                    <hr>
                </body>
                </html>

            """.format(name_return(num))


three_names.run(host=HOST, port=PORT)
