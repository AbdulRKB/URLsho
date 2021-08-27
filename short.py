import requests



def shortURL(url):
	res = requests.get(f'https://api.shrtco.de/v2/shorten?url={url}').json()['result']
	link1 = res['full_short_link']
	link2 = res['full_short_link2']
	link3 = res['full_short_link3']
	links = [link1,link2,link3]
	return links
