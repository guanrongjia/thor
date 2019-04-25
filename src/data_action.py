import os
from pyquery import PyQuery as pq
from lxml import etree
from tools import smart_decode


def get_data(content):
    try:
        doc = pq(etree.fromstring(content))
    except:
        doc = pq(content)

    screen_view = doc('.screen-view')
    for tr in screen_view.find('tr'):
        for td in pq(tr).find('td'):
            name = pq(td)('a').filter('.color-666')
            print name
        print ''


if __name__ == '__main__':
    file_dir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
    filename = '20190426005713.html'
    abs_path = os.path.join(file_dir, 'data', filename)

    with open(abs_path, 'r') as hfile:
        content = hfile.read()
        get_data(content)