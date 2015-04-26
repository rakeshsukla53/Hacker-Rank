__author__ = 'rakesh'

#Playing aroung with LOCU_API

import urllib2
import json

api = '14ec5d7993ac14e36c580589967a89f260e3b418'

url = 'https://api.locu.com/v1_0/venue/search/?'

local = 'NewPort Beach'
locality = local.replace(' ', '%20')

new_url = url + 'api_key=' + api + '&locality=' + locality

obj = urllib2.urlopen(new_url)

data = json.load(obj)

for abc in data['objects']:

    print abc['name']

