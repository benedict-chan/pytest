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

#Use findall here instead of split, because there's a lot of TEXT in between {{  }} XX {{ }}
re.findall(r"\{\{[^\{]*\}\}", content)


sline=re.findall(r"\{\{[^\{]*\}\}", content)[0]
re.split(r"\n\|", sline)
