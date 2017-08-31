from bottle import Bottle

dictio = {'bio': 'Biography', 'steve': 'Steve Jobs', 'pic': 'Pictures'}

app = Bottle()


@app.route('/')
def index():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Steve Jobs</title>
        </head>
        <body>
            <ol>
                <li><a href="/steve">Steve Jobs</a></li>
                <li><a href="/pic">Pictures</a></li>
                <li><a href="/bio">Biography</a></li>
            </ol>

        </body>
        </html>
        """


@app.route('/<word>')
def divider(word):
    return """
            <!DOCTYPE html>
                <html>
                <head>
                    <title>{}</title>
                </head>
                <body>
                    <ul>
                        <li><a href="/">home</a></li>
                    </ul>
                    <hr>
                    <center><h1>{}</h1><center>

                </body>
                </html>
            """.format(dictio[word.lower()], dictio[word.lower()])

app.run(host='localhost', port=83)
