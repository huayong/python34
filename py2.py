__author__ = 'Huayong'

import urllib.request as request
from bs4 import BeautifulSoup

def taobao(url):
    html = request.urlopen(url).read()
    data = html.decode('gbk')
    soup = BeautifulSoup(data)
    for list in soup.find_all('a'):
        print(list.string)

if __name__ == '__main__':
    url = 'http://www.taobao.com/?spm=a310q.2219005.1581860521.1.b9kUd4'
    taobao(url)
    print('git test')