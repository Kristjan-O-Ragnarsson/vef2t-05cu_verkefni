from bottle import Bottle, static_file

menu = """
        <ol>
            <li><a href="/steve">Steve Jobs</a></li>
            <li><a href="/pic">Pictures</a></li>
            <li><a href="/bio">Biography</a></li>
        </ol>
        """


def leagalize(title, body):
    """ for returning a leagl body of text """
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>{}</title>
            <link rel="stylesheet" type="text/css" href="/static/css/lo.css">
        </head>
        <body>
            <ol>
                <li><a href="/">Des home</a></li>
                <li><a href="/sp/steve">Steve Jobs</a></li>
                <li><a href="/sp/pic">Pictures</a></li>
                <li><a href="/sp/bio">Biography</a></li>
                <li><a href="/steve">Steve Jobs(fail)</a></li>
            </ol>
            <br>
            {}
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </body>
        </html>
    """.format(title, body)


class MyApp(Bottle):
    """ The most fun class i have ever debuged(
    a class for using bottle microframework) """
    def __init__(self):
        """ the constructor has all the routing """
        super(MyApp, self).__init__()
        self.route_dictio = {'steve': 'Steve Jobs', 'pic': 'Picture', 'bio': 'Biography'}
        self.err = {404: 'What u trying to do here?', '500': ''}
        self.title = 'Steve Jobs'
        self.route('/', callback=self.index)
        self.route('/sp/<page>', callback=self.sub_page)
        self.get('/static/img/<filepath:re:.*\.(png|jpg)>', callback=self.img)
        self.get('/static/css/<filepath:re:.*\.css>', callback=self.css)
        self.error(404, callback=self.error404)

    def error404(self, error):
        """ the 404 error """
        return '<center><h1>{}</h1></center><br>'.format(self.err[404])

    def img(self, filepath):
        """ for making images static """
        return static_file(filepath, root='./img')

    def css(self, filepath):
        """ for making css static """
        return static_file(filepath, root='./css')

    def index(self):
        """ the index page """
        l = '<img src="/static/img/stevejobs.jpg">' + 'lol'
        return leagalize(self.title, l)

    def sub_page(self, page):
        """ the rest of the site """
        return leagalize(self.route_dictio[page], '<img src="/static/img/stevejobs.jpg">')


app = MyApp()
if __name__ == '__main__':
    app.run(host='localhost', port=81, debug=True)
