from bottle import Bottle, static_file, request

app = Bottle()

cisco = ['cisco1.png', 'cisco.png', 'cisco - Copy (9).png', 'cisco - Copy (8).png', 'cisco - Copy (7).png',
         'cisco - Copy (6).png', 'cisco - Copy (5).png', 'cisco - Copy (4).png', 'cisco - Copy (3).png',
         'cisco - Copy (2).png']
cisco_text = ['Þetta er mynd af cisco logoinu', 'þetta er líka mynd af cisco lógóinu',
              'og ef þú gætir trúið því þá er þetta líka mynd af cisco logo',
              'því miður þá veitég eiginleka ekki hvað ég á að skrifa hérna',
              'Hérna eiga að vera upplysingar um myndina en þær eru ekki hérna',
              'one mississippi, two mississippi, three mississippi, for loop',
              'i have a copy of ccna oficial cert guide at home', 'promennt sér um ccna og ccent prófin á íslandi',
              'það er ekki til nein vandmál til að leisa', 'DaDa lugia']
# for returning a back button where is needed
do_back_or_not = lambda x: '<a href="/">Back</a><br>' if x else ''


def legalize(data, back=False):
    """ for making legal """
    return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>dada - this is a secret Cisco site</title>
                <link rel="stylesheet" type="text/css" href="/static/css/lo.css">
            </head>
            <body>
                <h1>[Um Title goes here]</h1>
                {}
                {}
            </body>
            </html>
    """.format(do_back_or_not(back) ,data)


def image_sys():
    """ for returning the imgaes """
    data = ''
    for i in range(len(cisco)):
        data += '<a href="/?ss={}"><img src="static/img/{}" title="{}"></a><br>'.format(i, cisco[i], cisco_text[i])
    return data


@app.route('/')
def index():
    """ the return og the site """
    num = request.query.ss
    print(num.isdigit())
    if num.isdigit():
        return legalize('<img src="static/img/{}" title="{}"><br><hr><h1>{}</h1>'.format(cisco[int(num)],
                                                                                         cisco_text[int(num)],
                                                                                         cisco_text[int(num)]),
                        back=True)
    else:
        return legalize(image_sys())


@app.get('/static/img/<num:re:.*\.(png|jpg|)>')
def img(num):
    """ for making images static """
    return static_file(num, root='./img')


@app.get('/static/css/<pth:re:.*\.css>')
def css(pth):
    """ for making css static """
    return static_file(pth, root='./css')

if __name__ == '__main__':
    app.run(host='localhost', port=81)