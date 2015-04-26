__author__ = 'rakesh'


import urllib2
import json

url = 'https://api.foursquare.com/v2/venues/search?oauth_token=4XPF3IPDAEN5TTQ2TFEYG4FNOKGTEHHHJNMSOOMQL0GB4VHG&v=20131016&ll=33.6167%2C%20-117.8975&intent=checkin'

#API are basically just a link

obj = urllib2.urlopen(url)

data = json.load(obj)


for line in data['response']['venues']:

    print line['name']  #it will give you all the APIs
    try:
        print line['contact']['phone']
    except Exception:
        pass
    try:
        print line['contact']['twitter']
    except Exception:
        pass







