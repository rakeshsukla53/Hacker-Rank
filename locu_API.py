__author__ = 'rakesh'

#Playing aroung with LOCU_API

import urllib2
import json

api = '14ec5d79a89f260e3b418'

#api is changed and it will not work

url = 'https://api.locu.com/v1_0/venue/search/?'

local = 'NewPort Beach'
locality = local.replace(' ', '%20')

new_url = url + 'api_key=' + api + '&locality=' + locality

obj = urllib2.urlopen(new_url)

data = json.load(obj)

for abc in data['objects']:

    print abc['name']

