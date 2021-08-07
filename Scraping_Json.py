import requests

json_data = requests.get('http://www.floatrates.com/daily/idr.json').json()

for data in json_data.values():
    print(data)
