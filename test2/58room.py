from urllib import request
from bs4 import BeautifulSoup
import random
import test11

host = 'https://wh.58.com/hezu/pn'

charset = 'utf-8'
debug = True

excel_save_path = '58rooms.xlsx'


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
        if item:
            test11.getNum(item.get_text())



def createHeaderIp():
    headers = {}
    ip = '%s.%s.%s.%s' % (random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255), random.randint(0, 255))
    headers['X-Forwarded-For'] = ip
    return headers

loadData(1)
