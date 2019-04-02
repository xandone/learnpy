from urllib import request
from bs4 import BeautifulSoup
import json
import random

area_name = ['武昌', '洪山', '东湖高新', '江夏', '江岸', '东西湖', '汉阳']
area_name_code = {'武昌': 13, '洪山': 8, '东湖高新': 13,
                  '江夏': 15, '江岸': 12, '东西湖': 10, '汉阳': 10}
area_wh = {}

host = 'http://www.jiangroom.com/queryRooms.html'
rooms_url = 'http://www.jiangroom.com/queryRoomsAsync?'

charset = 'utf-8'
debug = True


def main():
    if debug:
        for x in range(0, 10):
            createHeaderIp()
        # getAllData(x)


def getAreaCode(offset):
    params = 'offset=%d' % offset
    with request.urlopen(rooms_url + params) as resp:
        data = resp.read().decode(charset)
        bean = json.loads(data)
    for i in bean:
        name = i.get('premiseAddress')
        for j in area_name:
            if(j in name):
                area_wh[j] = int(i.get('usableArea'))
                break
    if len(area_wh) == len(area_name):
        print(area_wh.items())
        return
    else:
        offset += 1
        print('操作了' + str(offset + 1) + "次,area_wh=" + str(len(area_wh)))
        getAreaCode(offset)


def getAllData(page):
    params = 'offset=%d' % page
    headers = {''}
    with request.urlopen(rooms_url + params) as resp:
        data = resp.read().decode(charset)
        bean = json.loads(data)
    for i in bean:
        if i.get('usableArea') == area_name_code['武昌']:
            with open('F:/ab.txt', 'a+', encoding='UTF-8') as f:
                f.write(i.get('bedroomNameAbbr') + '\t' +
                        str(i.get('realityPrice')) + '\n')


def createHeaderIp():
    ip = '%s.%s.%s.%s' % (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255), random.randint(0, 255))
    headers = {'X-Forwarded-For': ip}
    print(headers)
    return headers

if __name__ == '__main__':
    main()
