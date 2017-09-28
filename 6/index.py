from bottle import Bottle, error, request, template
import csv, re
erro = {404: {'code': '404', 'joke': 'What are you doing here'}}
app = Bottle()
keys = ['name', 'email', 'tel', 'username', 'password']


def read_file():
    """ reads the file and imports the data """
    with open('lol.csv', 'r') as file:
        dump = []
        data = csv.reader(file, delimiter=';')
        for i in data:
            dump.append(i)
        return dump


def add_data_to_file(line):
    """ adds data to the file """
    with open('lol.csv', 'a') as file:
        dump = csv.writer(file, delimiter=';', lineterminator='\n')
        dump.writerow(line)


def passtest(string):
    pas = [0, 0]
    for char in string:
        if char.isdigit():
            pas[1] += 1
        if char.isalpha():
            pas[0] += 1
    return False if (len(string) >= 12 and pas[0] > 1 < pas[1]) else True

reg = re.compile("^(\+354)?\d{3}[ -]?\d{4}$")
test = []
username_list = []


for i in read_file():
    test.append(i)
    username_list.append(i[0])

print(username_list)
@app.error(404)
def error404(error):
    return template('error.tpl', erro[404])


@app.get('/')
def get_index():
    return template('main.tpl', {'name': 'Kristjab', 'email': 'b@b.B', 'tel': '+354662-5566', 'username': 'user',
                                 'password': 'PASSword123456', 'villa': 0, 'error': 'none'})


@app.post('/')
def post_index():
    info = {x: request.forms.get(x).strip().replace(' ', '_') for x in keys}
    print(info)
    if info['username'] in username_list:
        info['error'] = "Notenda nafn nú þegar í notkun"
        info['villa'] = 1
        return template('main.tpl', info)
    elif len(info['username']) < 4:
        info['error'] = "Notenda nafn of stutt"
        info['villa'] = 1
        return template('main.tpl', info)
    elif passtest(info['password']):
        info['error'] = "Likil orðið þitt er of lélegt"
        info['villa'] = 1
        return template('main.tpl', info)
    elif reg.match(info['tel']) is None:
        info['error'] = "vitlaust simanumer"
        info['villa'] = 1
        return template('main.tpl', info)
    elif '@' not in str(info['email']):
        info['error'] = "vitlaust email"
        info['villa'] = 1
        return template('main.tpl', info)
    else:
        test.append(info)
        username_list.append(info['username'])
        add_data_to_file((info['username'], info['password'], info['name'], info['email'], info['tel']))
        return template('msg', {'title': 'Sing up complete', 'msg': 'Þér tókst að búa til notanda'})

app.run(host='localhost', port=81)
