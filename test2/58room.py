from urllib import request
from bs4 import BeautifulSoup
import random
import test11
import pymysql

host = 'https://wh.58.com/hezu/pn'

charset = 'utf-8'
debug = True

excel_save_path = '58rooms.xlsx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

db = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123123',
    db='rooms',
    charset='utf8'
)

cursor = db.cursor()

sql = "INSERT INTO 58rooms (rname, price) VALUES ( '%s', %.2f )"


def main():
    if debug:
        print('')


def loadData(page):
    url = host + str(page)
    print(url)
    req = request.Request(url, None, createHeaderIp())
    resp = request.urlopen(req)
    soup = BeautifulSoup(resp, 'html.parser')
    data = soup.find('ul', class_='listUl')
    li = data.find_all('li')
    for i in li:
        item = i.find('b', class_='strongbox')
        item2 = i.find('a', class_='strongbox')
        print(item2.get_text())
        if item:
            price = test11.getNum(item.get_text())
            print(price)


def createHeaderIp():
    ip = '%s.%s.%s.%s' % (random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255), random.randint(0, 255))
    headers['X-Forwarded-For'] = ip
    return headers


def testdb():
    try:
        data = ('小区1', 360.59)
        cursor.execute(sql % data)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    db.close()


# testdb()
loadData(1)
