
import requests


def post(image, username, password, url=None):

    if not url:
        url = 'https://poster.de-captcher.com'

    data = {'username': username, 'password': password, 'pict_to': 0, 'pict_type': 0, 'function': 'picture2', 'submit': 'Send'}

    if isinstance(image, basestring):
        files = {'pict': open(image, 'rb')}
    else:
        files = {'pict': image}

    response = requests.post(url, data=data, files=files, verify=False)

    response.data = {}

    if response.content:
        try:
            resultcode, majorid, minorid, type_, timeout, text = response.content.split('|')
            response.data = {'resultcode': resultcode,
                             'majorid': majorid,
                             'minorid': minorid,
                             'type_': type_,
                             'timeout': timeout,
                             'text': text}
        except ValueError:
            pass

    return response


def balance(username, password, url=None):
    if not url:
        url = 'https://poster.de-captcher.com'

    data = {'username': username, 'password': password, 'function': 'balance', 'submit': 'Send'}

    response = requests.post(url, data=data, verify=False)

    return response
