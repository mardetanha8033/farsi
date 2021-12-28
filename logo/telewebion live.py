import requests
import json
from bs4 import BeautifulSoup
playlist = '#EXTM3U\n'
headers = {
    'authority': 'api.telewebion.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': '*/*',
    'device-token': 'c7cc3669-c540-49cb-a30d-ee44d131e6c9',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://telewebion.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://telewebion.com/',
    'accept-language': 'en-AU,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,fa;q=0.6',
}
params = (
    ('device', 'mobile'),
    ('logo_version', '4'),
    ('thumb_size', '240'),
    ('dvr', '1'),
)


response = requests.get(
    'https://telewebion.com/channels', headers=headers).text
soup = BeautifulSoup(response, 'html.parser')
item_list = soup.find_all('div', {'class': 'item mt-3 px-2'})[:62]
list_item = []
for item in item_list:
    channel_name = item.find(
        'a', {'class': 'box h-100 pointer d-block'})['href']
    channel_name = channel_name.split('/')[2]

    respons = requests.get(
        f'https://api.telewebion.com/v3/channels/{channel_name}/details', headers=headers, params=params).text
    data = json.loads(respons)['data'][0]
    link = data['links'][0]['link']
    name = data['channel']['descriptor'].capitalize()
    logo = data['channel']['image_name']
#print(name, link, logo)
    playlist += '#EXTINF:-1 tvg-id="(no tvg-id)" tvg-name="%s" tvg-logo="%s" group-title="IRIB Channels",%s\n%s\n' % (
        name, logo, name, link)
# print(playlist)
    f = open("telewebionlive.txt", "w+")
    f.write(playlist)
    f.close()
