import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'film2sun.fun',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-AU,en;q=0.9',
    'cookie': '_ga_G7BJFYC6LF=GS1.1.1633751994.1.0.1633751994.0; _ga=GA1.1.1893879513.1633751995',
}

response = requests.get('https://film2sun.fun/dubbed', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

item_list = soup.find_all('article', {'class' : 'box'})
for item in item_list:
    name = item.find('h2', {'class' : 'title-text'}).text[12:]
    link = item.find('h2', {'class' : 'title-text'}).a['href']
    description = item.find('p', {'class' : 'summary en_plot'}).text
    icon = item.find('img', {'class' : 'attachment-poster size-poster wp-post-image'})['src']
    
    
#Get each movies links
import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'film2sun.fun',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-AU,en;q=0.9',
    'cookie': '_ga_G7BJFYC6LF=GS1.1.1633751994.1.0.1633751994.0; _ga=GA1.1.1893879513.1633751995',
}

response = requests.get('https://film2sun.fun/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d9%81%db%8c%d9%84%d9%85-candyman-2020.html', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

item_list = soup.find_all('div', {'class' : 'each-quality active'})[:2]
for item in item_list:
    name = item.find('ul', {'class' : 'dl-info'}).text
    links = item.find('ul', {'class' : 'links'})
    for link in links:
        linkk = link.a['href']
        title = link.find('ul', {'class' : 'dl-info'}).text[:-9]
        print(title)
