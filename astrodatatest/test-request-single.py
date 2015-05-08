import json, requests
import urllib


"""
url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)


resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
resp.json()

with open('data.json', 'w') as f:
    json.dump(data, f)
"""


#Below the url is work

#http://www.astro.com/wiki/astro-databank/api.php?action=query&format=json&prop=revisions&rvprop=content&titles=Jobs%2C_Steve
#http://www.astro.com/wiki/astro-databank/api.php?action=query&format=json&prop=revisions&rvprop=content&titles=Jobs%2C_Steve

titles = "Jobs,_Steve"

params = { 
	"format":"json", 
	"action":"query", 
	"prop":"revisions", 
	"rvprop":"content" 
}
params.update({"titles":titles})

api_url = "http://www.astro.com/wiki/astro-databank/api.php?"

resp = requests.get(url=api_url, params=params)
single_data = resp.json()
with open('single_data.json', 'w') as f:
    json.dump(single_data, f)
#params["titles"] = "%s" % urllib.quote(titles.encode("utf8"))
#qs = "&".join("%s=%s" % (k, v)  for k, v in params.items())
#url = "http://www.astro.com/wiki/astro-databank/api.php?%s" % qs


#Test requests by pageids
#http://www.astro.com/wiki/astro-databank/api.php?action=query&format=json&prop=revisions&rvprop=content&pageids=29562

pageid = 29562

params = { 
    "format":"json", 
    "action":"query", 
    "prop":"revisions", 
    "rvprop":"content" 
}
params.update({"pageids":pageid})

api_url = "http://www.astro.com/wiki/astro-databank/api.php?"

resp = requests.get(url=api_url, params=params)
single_data = resp.json()
with open('single_data_pageid.json', 'w') as f:
    json.dump(single_data, f)
