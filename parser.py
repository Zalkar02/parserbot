from bs4 import BeautifulSoup as bs
import requests
from urllib import request, error


headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'} 

url = 'https://kg.akipress.org/cat:1/' # базовый урл

def akipress_pars(url, headers):
    data = []

    session  = requests.Session() #иммитация браузера
    request = session.get(url, headers = headers)
    if request.status_code == 200: # статус код ответ сервера
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs= {'class': 'elem'})
        for div in divs[:20]:
            title = div.find('a').text
            href = div.find('a')['href'] 
            data.append({
                'title': title,
                'href': href
            })
        print(data)
    else:
        print('ERROR')




akipress_pars(url, headers)