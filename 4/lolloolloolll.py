import time
news = [{'title': 'þessi snígil vann heimsmetið', 'author': 'gus@tskoli.is',
  'content': 'Þessi snígil vann heimsmetið í að hoppa ', 'links': 'links', 'img': '600.jpg'},
 {'title': 'þessi snígil vann heimsmetið', 'author': 'gus@tskoli.is',
  'content': 'Þessi snígil vann heimsmetið í að hoppa ', 'links': 'links'},
{'title': 'þessi snígil vann heimsmetið', 'author': 'gus@tskoli.is',
  'content': 'Þessi snígil vann heimsmetið í að hoppa ', 'links': 'links'}
 ]
home = {'title': 'Frétta síðan mikla',
        'content': 'Hin mikkla fræga mikilvæga frétta síða',
        'ne': [{'title': x['title'], 'author': x['author'], 'content': x['content']} for x in news],
        'links': 'links'}
for i in home['ne']:
    print(i['title'])
    print(i['author'])
    print(i['content'])
    time.sleep(1)