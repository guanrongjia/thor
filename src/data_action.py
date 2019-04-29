# coding=utf8
import os
from pyquery import PyQuery as pq
from lxml import etree
from HTMLParser import HTMLParser
from tools import smart_decode
import json


def get_data(content):
    print 'start filter html content'
    content = smart_decode(content)
    try:
        doc = pq(etree.fromstring(content))
    except:
        doc = pq(content)
    screen_view = doc('.screen-view')
    page_data = {'game_in_progress': [], 'game_finished': []}
    print 'filter current game data'
    for tr in screen_view.find('tr'):
        simple_game_data = []
        for td in pq(tr).find('td'):
            name = pq(td)('a').filter('.color-666')
            score = pq(td)('b')
            if name:
                team_name = HTMLParser().unescape(name.text()),
                simple_game_data.append(team_name[0].strip() if team_name else '')
            if score:
                current_score = HTMLParser().unescape(score.text()),
                simple_game_data.append(current_score[0].strip() if current_score else '')

        if len(simple_game_data) == 3:
            page_data['game_in_progress'].append({u'team1': simple_game_data[0],
                                                   u'current_score': simple_game_data[1],
                                                   u'team2': simple_game_data[2]})
        elif len(simple_game_data) == 2:
            page_data['game_finished'].append({u'team1': simple_game_data[0],
                                               u'team2': simple_game_data[1]})
    # print json.dumps(page_data, ensure_ascii=False)
    return page_data


if __name__ == '__main__':
    file_dir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
    filename = '20190429214608.html'
    abs_path = os.path.join(file_dir, 'data', filename)

    with open(abs_path, 'r') as hfile:
        content = hfile.read()
        get_data(content)