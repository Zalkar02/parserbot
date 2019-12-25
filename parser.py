from bs4 import BeautifulSoup
import requests

def get_url(url):                
    result = requests.get(url)
    return result.text


def get_data(html):                            # Парсит указоный сайт и находит нужные теги
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_= "elem")

	d = {}
	num = 0

	for item in items[:20]:
		num += 1
		i = item.find('a')
		item_text = i.get_text()
		d[num] = f'{item_text}'
	return d

def get_str(html):                                 # Парсит указоный сайт и находит нужные теги
	soup = BeautifulSoup(html, 'html.parser')
	x = str(soup.find('h1').get_text())
	y = soup.find_all('p')
	z = ''
	for i in y:
		z += str(i.get_text())
	return f'{x} \n{z}'

def get_tit(html, article):                   # Ищет нужую ссылку
	soup = BeautifulSoup(html, 'html.parser')

	items = soup.find_all('div', class_= "elem")

	for item in items:
		if article == item.find('a').get_text():
			url = str(item.find('a').get('href'))
			total = get_url(url)
			return get_str(total)

def main():                               # Функция возрощает словарь
    url = 'http://kg.akipress.org/cat:1.'
    total = get_url(url)
    return get_data(total)

def title(article):                       # Возрощает фсю статью 
	url = 'http://kg.akipress.org/cat:1.'
	total = get_url(url)
	return get_tit(total, article)

if __name__ == '__main__':     # Как пользыватся функциями
	for k,v in main().items():   
		print(f'{k}) {v}')
	print(title('Запуск мусоросортировочного полигона планируется в декабре 2020 года, - вице-мэр'))