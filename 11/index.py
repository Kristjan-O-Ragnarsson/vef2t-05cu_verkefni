import bottle
import pymysql
import references

conn = pymysql.connect(
    host=references.SQLHOST,
    user=references.USER,
    port=references.SQLPORT,
    password=references.PASS,
    database='1308002620_vef2Verk11'
)


def sql_get(query, *args):
    cur = conn.cursor()
    cur.execute(query.format(*args))
    data = cur.fetchall()
    cur.close()
    return data


def sql_do(query, *args):
    cur = conn.cursor()
    cur.execute(query.format(*args))
    conn.commit()
    cur.close()


def sql_mod_car(query, one, two, three, four, five, six, seven, eight):
    cur = conn.cursor()
    cur.execute(query.format(one, two, three, four, five, six, seven, eight))
    conn.commit()
    cur.close()


@bottle.route('/')
def index():
    return bottle.template('inde.html')


@bottle.get('/car')
def get_car():
    return bottle.template('car.html', {'multi': False})


@bottle.post('/car')
def post_car():
    data = sql_get('select * from bilar where skraningarnumer = "{}";', bottle.request.forms.name)
    return bottle.template('car_p.html', {'results': data, 'multi': True, 'id': 'car'})


@bottle.get('/del')
def get_del():
    data = sql_get('select skraningarnumer from bilar;')
    return bottle.template('car_d.html', {'data': data, 'action': 'del', 'multi': False})


@bottle.post('/del')
def post_del():
    sql_do('delete from bilar where skraningarnumer =  "{}";', bottle.request.forms.car)
    return bottle.redirect('/')


@bottle.get('/update')
def get_update():
    data = sql_get('select skraningarnumer from bilar;')
    return bottle.template('car_d.html', {'data': data, 'action': 'update', 'multi': False})


@bottle.post('/update')
def post_update():
    data = sql_get('select * from bilar where skraningarnumer =  "{}";', bottle.request.forms.car)
    return bottle.template('car_u.html', {
        'action': 's/up',
        "number": data[0][0],
        "factoryNumber": data[0][2],
        "type": data[0][1],
        "registeredAt": data[0][3],
        "status": data[0][7],
        "nextCheck": data[0][6],
        "pollution": data[0][4],
        "weight": data[0][5],
        'multi': True,
        'id': '/update'
    })


@bottle.post('/s/up')
def update():
    sql_mod_car('update bilar set Tegund = "{}",'
                ' verksmidjunumer = "{}",'
                ' skraningardagur = "{}",'
                ' co2 = "{}", þyngd = "{}",'
                ' skodun = "{}", stada = "{}"'
                ' where skraningarnumer = "{}";',
                bottle.request.forms.type,
                bottle.request.forms.factoryNumber,
                bottle.request.forms.registeredAt,
                bottle.request.forms.pollution,
                bottle.request.forms.weight,
                bottle.request.forms.nextCheck,
                bottle.request.forms.status,
                bottle.request.forms.number
                )

    return bottle.redirect('/')


@bottle.get('/add')
def get_add():
    return bottle.template('car_u.html', {
            'action': 'add',
            "number": "AA031",
            "factoryNumber": "VF37ENFZE32286866",
            "type": "PEUGEOT",
            "registeredAt": "26.02.1998",
            "status": "Í lagi",
            "nextCheck": "01.01.2013",
            "pollution": "",
            "weight": "1120",
            'multi': False
        })


@bottle.post('/add')
def post_add():
    sql_mod_car('insert into '
                'bilar '
                'values '
                '("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");',
                bottle.request.forms.number,
                bottle.request.forms.type,
                bottle.request.forms.factoryNumber,
                bottle.request.forms.registeredAt,
                bottle.request.forms.pollution,
                bottle.request.forms.weight,
                bottle.request.forms.nextCheck,
                bottle.request.forms.status
                )
    return bottle.redirect('/')


@bottle.get('/s/<path:re:.*\.(png|jpg|json|css)>')
def static(path):
    return bottle.static_file(path, root='./st')

bottle.run(host='localhost', port=81, reloader=False)
