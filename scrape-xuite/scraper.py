
"""
Date: 2015-06-23

To access the album
1. get the album thumbnail link:
2. change the thumbnail to: _x
3. Loop through as unix time to get all the links

"""

import requests
import scraperwiki

def start_process():
	total_page = 100
	success_page = 0
	for counter in range(range_time_from, range_time_to):
		if success_page >= total_page:
			break
		url = "http://{A}.share.photo.xuite.net/{user_id}/x{A}{B}{C}{E}xx/{album_id}/%s_x.jpg" % counter
		resp = requests.head(url=url)
		if resp.ok:
			if 'x-share-file' in resp.headers:
				file_name = resp.headers['x-share-file']
				record_dict = {"file_name": file_name, "url": url}
				success_page = success_page + 1
				print url
				scraperwiki.sqlite.save(unique_keys=['file_name'], data=record_dict, table_name="image")
				break
			pass
	pass

def get_full_size():
	url = 'http://o.{A}.photo.xuite.net/{A}/{B}/{C}/{E}/{user_id}/{album_id}/{image}.jpg'
	headers = {'Accept': 'image/webp,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64)', 'Referer':'http://photo.xuite.net/'}
	resp = requests.head(url=url, headers=headers)


if __name__ == "__main__":
	start_process()		