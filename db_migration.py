import sqlite3
import requests
from pytils.translit import slugify
from bs4 import BeautifulSoup


URL = 'http://piek.ru/catalog/elektroprivody/pem-a/'
HEADERS = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    r.encoding = 'utf-8'
    return r

def get_content(html):
    table_num = str(3)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("table:nth-of-type("+ table_num +")", class_='simple-little-table')   # номер таблицы на странице
    print(items)
    tr_list = soup.select("table:nth-of-type("+ table_num +") > tr", class_='simple-little-table')
    count_tr = len(tr_list)
    container = []
    print(count_tr - 1)


    for item in items:
        for i in range(1, count_tr):
            row = i + 1
            title = item.select("tr:nth-child("+ str(row) +") td:nth-child(2)")[0].text
            a = item.select("tr:nth-child(" + str(row) + ") td:nth-child(3)")[0].text
            b = item.select("tr:nth-child(" + str(row) + ") td:nth-child(4)")[0].text
            c = item.select("tr:nth-child(" + str(row) + ") td:nth-child(5)")[0].text

            container.append(
                {
                    'title': title,
                    'a' : a,
                    'b': b,
                    'c': c,
                }
            )
        return container


def mod_table(a,b,c):
    content = '''<table style="border-collapse: collapse; height: 150px; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 48.5656%;">Номинальный крутящий момент на выходном валу, Nm</td>
<td style="width: 51.4344%; text-align: center;">''' + a + '''</td>
</tr>
<tr>
<td style="width: 48.5656%;">Номинальное время полного хода выходного вала, S</td>
<td style="width: 51.4344%; text-align: center;">''' + b + '''</td>
</tr>
<tr>
<td style="width: 48.5656%;">Номинальный полный ход выходного вала, обороты</td>
<td style="width: 51.4344%; text-align: center;">''' + c + '''</td>
</tr>
</tbody>
</table>
'''

    return content

def next_id():
    cur.execute("SELECT * FROM mainapp_modification ORDER BY id DESC LIMIT 1;")
    res = cur.fetchone()
    last_record_id = res[0]
    next_id = last_record_id + 1
    return next_id

def slug_mod(title):
    slug_mod = slugify(title)
    return slug_mod



# c.execute('''CREATE TABLE empoyess
#              (date text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO empoyess VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

html = get_html(URL)
container = get_content(html.text)
db = sqlite3.connect("db.sqlite3")
print('Предварительный просмотр:')
for i in range(0, len(container)):
    print(container[i])
accept = input('Для внесения изменений введи True:')
parent_id = input("Идентификатор группы: ")
if accept == 'True':
    for i in range(0, len(container)):
        title = container[i].get('title')
        title = 'МЭО-' + title
        a = container[i].get('a')
        b = container[i].get('b')
        c = container[i].get('c')
        cur = db.cursor()
        content = mod_table(str(a), str(b), str(c))
        cur.execute("INSERT INTO mainapp_modification VALUES (?,?,?,?,?)", (next_id(), slug_mod(title), title, content, parent_id))

db.commit()
db.close()

    # for one in i.values():
    #     print(one)
    # content = mod_table(str(parse_content[0]),str(2),str(3))
    # print('')
    # print(parse_content.values[1])
    # c.execute("INSERT INTO mainapp_modification VALUES (?,?,?,?,?)", (next_id(), slug_mod(title), title, content, 6))


