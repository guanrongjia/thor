import json
from dom_action import get_dom_html
from data_action import get_data


def main():
    dom_html = get_dom_html()
    game_data = get_data(dom_html)
    return game_data


if __name__ == '__main__':
    print json.dumps(main(), ensure_ascii=False)
