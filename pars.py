import requests
from typing import Tuple 
from bs4 import BeautifulSoup

def get_content(link: str) -> str:
	return requests.get(url=link).text

def write_content_to_file(content:str, filename:str) -> Tuple[bool, str]:
	try:
		with open(filename, 'w') as text_file:
			text_file.write(content)
		return True, 'Success'
	except Exception as e:
		return False, str(e)


if __name__ == '__main__':
	link = 'https://kg.akipress.org/cat:1/'
	content = get_content(link=link)
	soup = BeautifulSoup(content, features='html.parser')
	posters = soup.find_all('div', attrs = {'class': 'news_list'})
	news_list = []

	for item in posters:
		if item.find('a') is not None:
			element = item.find('a')
			span = item.find('span')

			news_list.append(
			  {
				'title': element.text if element else None,
				'time': span.text if span else None,
				'url': element['href'] if element else None
			  }
			)




	



