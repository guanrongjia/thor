import types


def smart_decode(text):
    if type(text) == types.UnicodeType:
        return text
    elif not isinstance(text, types.StringTypes):
        text = str(text)
    try:
        return text.decode('utf8')
    except UnicodeDecodeError:
        try:
            return text.decode('gb2312')
        except UnicodeDecodeError:
            pass
    return text
