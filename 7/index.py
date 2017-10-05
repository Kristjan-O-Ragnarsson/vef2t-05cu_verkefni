from bottle import Bottle, request, redirect, response, template

app = Bottle()

HOST = 'localhost'
PORT = 81

_user = 'Admin'
_pass = 'TooR'
cookie_key = '%Ldd3h2YQ0zslY*L1VAl5N7E6yXSgn@QgfMOSg2yKj2BO^VS0&JH#wix!3Zldmh!'
skip_keys = ['coinhive-captcha-token']


def login(data, keys, key_ord):
    if data[keys[key_ord['u']]] == _user and data[keys[key_ord['p']]] == _pass:
        return True
    else:
        return False


@app.route('/')
def index():
    return template('main.tpl', {'action': '/l/sec', 'key': 'UN5vqGpZBcJkJ4Qlx9MWXFHEg0pgOExy', 'user': 'USER',
                                 'passw': 'PASS', 'mon': False})


@app.post('/l/sec')
def admin_login():
    keys = [x for x in request.forms if x not in skip_keys]
    key_ord = {'u': keys.index('user'), 'p': keys.index('password')}
    info = {x: request.forms.get(x) for x in keys}
    print(info[keys[key_ord['u']]] == _user)
    print(info[keys[key_ord['u']]])
    print(_user)

    if login(info, keys, key_ord):
        response.set_cookie('ThisCookieIsNotStealingInfo', 'What are you doing looking at this cookie',
                            secret=cookie_key)
        return template('msg', {'title': 'Some Secret Admin Site with a huge vulnerability', 'msg': 'Leynisíða',
                                'succ': 1})

    elif info[keys[key_ord['u']]] != _user:
        return template('msg.tpl', {'title': 'U need a Medical', 'msg': 'Þetta notanda nafn er flott en því'
                                                                        ' miður ekki rétt', 'succ': 0})
    elif info[keys[key_ord['p']]] != _pass:
        return template('msg.tpl', {'title': 'U need a Medical', 'msg': 'Þetta lykil orð er flott en því'
                                                                        ' miður ekki rétt', 'succ': 0})


@app.get('/x/logout')
def logout():
    response.set_cookie('ThisCookieIsNotStealingInfo', 'NUKE', expires=0)
    return redirect('/')


app.run(host=HOST, port=PORT)
