from bottle import Bottle
HOST = 'localhost'
PORT = 81

hello_world = Bottle()


@hello_world.route('/hallo')
def hello():
    return """
        <!DOCTYPE html>
            <html>
            <head>
                <title>Bottle site</title>
            </head>
            <body>
                <h1>Halló heimur</h1>

            </body>
            </html>
    """

hello_world.run(host=HOST, port=PORT)