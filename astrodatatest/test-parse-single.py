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

#Use findall here instead of split, because there's a lot of TEXT that we don't need in between {{  }} XX {{ }}
template_lines = re.findall(r"\{\{[^\{]*\}\}", content)


#Test of spliting each line
#sline=re.findall(r"\{\{[^\{]*\}\}", content)[0]
#re.split(r"\n\|", sline)


for sline in template_lines:
	template_split = re.split(r"\n\|", sline)
	#Fix the data
	template_split[0] = template_split[0].replace("{{", "") #First line will start with {{
	template_split[-1] = template_split[-1].replace("\n}}", "") #Last line has \n}} at the end, 
	#get template name
	template_name = template_split[0]
	record_string_list = template_split[1:] #These record string are in the format of ["X1=YY", "X2=ZZ"...]
	record_list_list = map(lambda x: re.split("=", x) , record_string_list) #These list list is [ ["X1", "YY"], ["X2", ZZ"] , ...]
	

