import json
from pprint import pprint

import re

with open('single_data.json') as data_file:    
    data = json.load(data_file)

pprint(data)

#data["query"]["pages"]["29562"]["revisions"]
#type(data["query"]["pages"]["29562"]["revisions"]) < list , len == 1

text = data["query"]["pages"]["29562"]["revisions"][0]["*"]

pattern = "__NOTOC__[\W{}+]"
re.split(pattern, text)
content = re.split(pattern, text)[1]


re.findall(r"\{\{[^\{]*\}\}", content)

