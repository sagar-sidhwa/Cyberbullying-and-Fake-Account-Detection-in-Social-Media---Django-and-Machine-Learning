# Website Used is geoJS
# Link = 'https://get.geoJS.io/'
# Link for IP = 'https://get.geoJS.io/v1/ip.json'
# geo_url = 'https://get.geoJS.io/v1/ip/geo/'+ipAdd+'.json'


import requests

ip_request = requests.get('https://get.geoJS.io/v1/ip.json')
ipAdd = ip_request.json()['ip']
print(ipAdd)

url = 'https://get.geoJS.io/v1/ip/geo/'+ipAdd+'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()

#print(geo_data['city'])
#print(type(geo_data))
print(geo_data)
