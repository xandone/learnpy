import urllib.request
from bs4 import BeautifulSoup

host = 'https://book.douban.com/top250?'
imgPath = 'F:/imgs/'


def getImgSrc(x):
    params = 'start=%d' % x
    hosturl = host + params
    print(hosturl)
    response = urllib.request.urlopen(hosturl)
    soup = BeautifulSoup(response, 'html.parser')
    data = soup.find('div', class_='indent')
    return data


def loadimgs(data):
    src = data.find_all('tr', class_='item')
    for i in src:
        imgSrc = i.find('a', class_='nbg').find('img').get('src')
        name = i.find('div', class_='pl2').find('a').get('title')
        print(name + '   ' + imgSrc)
        urllib.request.urlretrieve(imgSrc, imgPath + name + '.jpg')

if __name__ == '__main__':
    for x in range(0, 125, 25):
        loadimgs(getImgSrc(x))
