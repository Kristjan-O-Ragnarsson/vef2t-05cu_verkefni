"""
Kristjan O.
Verk 10
"""

import bottle
import pymysql
import bleach
import references

conn = pymysql.connect(
    host=references.SQLHOST,
    user=references.USER,
    port=references.SQLPORT,
    password=references.PASS,
    database='1308002620_vef2Verk10'
)


key_ord = {'u': 'username', 'p': 'password'}


def get_username_list():
    cur = conn.cursor()
    cur.execute('SELECT user from user;')
    listi = []
    for i in cur:
        listi.append(i[0])
    cur.close()
    return listi


@bottle.route('/')
def index():
    """ The front page """
    return bottle.template('index.tpl')


@bottle.get('/login')
def get_login():
    """ get response for login """
    return bottle.template('login.tpl', {'action': '/login', 'username': '', 'password': ''})


@bottle.post('/login')
def post_login():
    """ post response for login
        This is a bad login system"""
    cur = conn.cursor()
    keys = [x for x in bottle.request.forms]
    items = {x: bleach.clean(bottle.request.forms.get(x)) for x in keys}
    cur.execute("SELECT * from user;")
    for row in cur:
        print(row)
        if items[key_ord['u']] == row[0] and items[key_ord['p']] == row[1]:
            cur.close()
            return bottle.template('hidd.tpl')
    cur.close()
    return bottle.template('login.tpl', {'action': '/login', 'username': items[key_ord['u']], 'password': ''})


@bottle.get('/signup')
def get_signup():
    """ get response for signup """
    return bottle.template('signup.tpl', {'action': '/signup', 'username': '', 'password': '', 'villa': 0})


@bottle.post('/signup')
def post_signup():
    cur = conn.cursor()
    keys = [x for x in bottle.request.forms]
    items = {x: bleach.clean(bottle.request.forms.get(x)) for x in keys}
    print(items)
    username_list = get_username_list()
    print(username_list)
    if items[key_ord['u']] in username_list:
        print('in')
        cur.close()
        return bottle.template('signup.tpl', {'action': '/signup', 'username': items[key_ord['u']], 'password': '',
                                              'villa': 1, 'error': 'Notenda nafn þegar í notkun'})
    else:
        print('out')
        cur.execute("INSERT INTO `user`(`user`, `pass`) VALUES ('{}', '{}')".format(items[key_ord['u']], items[key_ord['p']]))
        conn.commit()
        cur.close()
        return 'notandi bætt við'


bottle.run(
    host=references.HOST,
    port=references.PORT
)

cur.close()