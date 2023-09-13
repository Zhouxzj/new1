import json
import requests

API_KEY = 'XXX'


def get_geo(add):
    add = str(add).replace('', '+')
    quiry = \
        'https://maps.googleapis.com/maps/api/geocode/' \
        'json?address={}&key={}'.format(add, API_KEY)
    response = requests.get(quiry)
    j = json.loads(response.text)
    return j.get('results')[0].get('geometry').get('viewport').get('southwest').values()


def get_timezone(val1, val2):
    quiry = \
        'https://maps.google.com/maps/api/timezone/json?location={},{}&timestamp=1412649030&key={}'.format(val1, val2,
                                                                                                           API_KEY)
    response = requests.get(quiry)
    j = json.loads(response.text)
    return j.get('timeZoneName'), j.get('timeZoneId')


if __name__ == '__main__':
    print(get_timezone(34.68, 113.65))
    address = input('Please input address:')
    q = list(get_geo(address))

    print(get_timezone(q[0], q[1]))
