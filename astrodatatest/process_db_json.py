import scraperwiki
import json
from pprint import pprint

import re

def start_process():
	page_id_list = scraperwiki.sqlite.select(" page_id FROM data WHERE processed = 0 limit 1")
	for page_id in page_id_list:
		db_json_str = scraperwiki.sqlite.select(" json_str FROM data WHERE page_id = %s" % page_id)
		json_dict = db_json_str[0]
		json_str = json_dict["json_str"]
		spage_id = str(page_id)
		json_data = json.loads(json_str)
		parse_json_str_for_page_id(spage_id, json_data)
	pass


def parse_json_str_for_page_id(spage_id, data):
	try:
		#data["query"]["pages"]["29562"]["revisions"]
		#type(data["query"]["pages"]["29562"]["revisions"]) < list , len == 1

		text = data["query"]["pages"][spage_id]["revisions"][0]["*"]

		pattern = "__NOTOC__[\W{}+]"
		#re.split(pattern, text)
		content = re.split(pattern, text)[1]

		#Use findall here instead of split, because there's a lot of TEXT that we don't need in between {{  }} XX {{ }}
		template_lines = re.findall(r"\{\{[^\{]*\}\}", content)

		#domain_id is the user id, we may need to pass it to most of the templations to create DB relationship
		domain_id = re.split("=", re.split(r"\n\|", template_lines[0])[1])[1]
		#Test of spliting each line
		#sline=re.findall(r"\{\{[^\{]*\}\}", content)[0]
		#re.split(r"\n\|", sline)

		#sline = template_lines[0]
		for sline in template_lines:
			template_split = re.split(r"\n\|", sline)
			#Fix the data
			template_split[0] = template_split[0].replace("{{", "") #First line will start with {{
			template_split[-1] = template_split[-1].replace("\n}}", "") #Last line has \n}} at the end, 
			#get template name
			template_name = template_split[0]
			record_string_list = template_split[1:] #These record string are in the format of ["X1=YY", "X2=ZZ"...]
			record_list_list = map(lambda x: re.split("=", x) , record_string_list) #These list list is [ ["X1", "YY"], ["X2", ZZ"] , ...]
			record_dict = dict(record_list_list)
			store_dict_to_db(domain_id, template_name, record_dict)
	except Exception, e:
		print 'Fail parsing page %s' % page_id
	finally:
		pass

def process_user(domain_id, template_name, record_dict):
	record_dict.update({"user_id":domain_id})
	print "process_user, just save to db %s" % "user"
	pass

def process_user_linked(domain_id, template_name, record_dict):
	record_dict.update({"user_id":domain_id})
	db_mapper = {
	  'ASTRODATABANK_img': "image",
	  'ASTRODATABANK_evn': "event",
	  'ASTRODATABANK_rel': "relationship",
	}
	table_name = db_mapper[db_mapper]
	print "process %s, just save to db %s", (template_name, table_name)
	pass

def process_category(domain_id, template_name, record_dict):
	record_dict.update({"category_id":record_dict["CodeID"]})
	user_cat_relation_dict = {user_id: domain_id, category_id: record_dict["CodeID"]}
	print "process_category, just save to db %s" % "category"
	print "process_user_category, just save to db %s" % "user_category"
	pass


def store_dict_to_db(domain_id, template_name, record_dict):
	try:
		templates = {
		  'ASTRODATABANK_dma': process_user,
		  'ASTRODATABANK_img': process_user_linked,
		  'ASTRODATABANK_evn': process_user_linked,
		  'ASTRODATABANK_rel': process_user_linked,
		  'ASTRODATABANK_cat': process_category,
		}[value](domain_id, record_dict)
		#scraperwiki.sqlite.save(unique_keys=['id'], data=data, table_name="data")
		pass
	except Exception, e:
		print 'Fail storing to db domain_id %s, template_name %s' % (domain_id, template_name)
	else:
		pass
	finally:
		pass

if __name__ == "__main__":
	start_process()