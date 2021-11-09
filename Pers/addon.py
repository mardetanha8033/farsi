import binascii
import sys
import requests
import xbmcplugin
import xbmc
import xbmcgui
import re
import json
import pyaes
import base64
from binascii import unhexlify
from bs4 import BeautifulSoup
from urllib.parse import quote, urlencode, urlparse
from urllib.parse import quote_plus, parse_qsl
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
handle = int(sys.argv[1])
cookies = {
    'language': 'en',
    'PHPSESSID': 'e49cdffe316aeffecdae2b670e381dc7',
    'ageconfirm': '1',
}
post_headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'http://protonvideo.to',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'http://protonvideo.to/',
    'Accept-Language': 'en-AU,en;q=0.9',
}

empire_cookies = {
    'language': 'en',
    'PHPSESSID': '6fef9f659bdf38eb22c0c81ed479bd69',
    'ageconfirm': '1',
    'viewed_ids': '3555,4346,4344,4348,1163',
}

empire_headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://sex-empire.tv/en/',
    'Accept-Language': 'en-AU,en;q=0.9',
}


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-AU,en;q=0.9',
}

url = 'http://film-adult.org/en/films/'
base_url = 'http://film-adult.org'
base_categories = 'http://film-adult.org/en/collections/'
base_top = 'http://film-adult.org/en/top100.html'
base_new = 'http://film-adult.org/en/movies/datepost/2021/'
base_usa = 'http://film-adult.org/en/movies/country/USA/'
base_italy = 'http://film-adult.org/en/movies/country/Italy/'
base_france = 'http://film-adult.org/en/movies/country/France/'
base_spain = 'http://film-adult.org/en/movies/country/Spain/'
base_eroupe = 'http://film-adult.org/en/movies/country/Europe/'
base_scenes = 'http://film-adult.org/en/videos/'
base_dorcel = 'http://film-adult.org/en/films/marc_dorcel/'
base_wicked = 'http://film-adult.org/en/films/wicked-pictures/'
base_digital = 'http://film-adult.org/en/films/digital-playground/'
base_mario = 'http://film-adult.org/en/films/mario-salieri/'
base_private = 'http://film-adult.org/en/films/private/'
base_classic = 'http://film-adult.org/en/films/vintage/'
base_paradoies = 'http://film-adult.org/en/films/parodies/'
empire_base = 'http://sex-empire.tv'
empire_categories = 'http://sex-empire.tv/en/collections/'
empre_latest = 'http://sex-empire.tv/en/watch/year/2021/'
empire_fullHD = 'http://sex-empire.tv/en/fullhd-porn-movie/'
empire_top = 'http://sex-empire.tv/en/top.html'
empire_scenes = 'http://sex-empire.tv/en/porno-video/'
empire_usa = 'http://sex-empire.tv/en/watch/country/USA/'
empire_italy = 'http://sex-empire.tv/en/watch/country/Italy/'
empire_france = 'http://sex-empire.tv/en/watch/country/France/'
empire_spain = 'http://sex-empire.tv/en/watch/country/Spain/'
empire_eroupe = 'http://sex-empire.tv/en/watch/country/Europe/'
empire_dorcel = 'http://sex-empire.tv/en/marc_dorcel/'
empire_wicked = 'http://sex-empire.tv/en/wicked-pictures/'
empire_digital = 'http://sex-empire.tv/en/digital-playground/'
empire_mario = 'http://sex-empire.tv/en/mario-salieri/'
empire_private = 'http://sex-empire.tv/en/private/'
empire_classic = 'http://sex-empire.tv/en/vintagexxx/'
empire_paradoies = 'http://sex-empire.tv/en/porno-parodies/'
empire_tabo = 'http://sex-empire.tv/en/porno-filmy/studios/pure-taboo/'
empire_hustler = 'http://sex-empire.tv/en/hustler/'
empire_sensation = 'http://sex-empire.tv/en/porno-filmy/studios/new-sensations/'
empire_daring = 'http://sex-empire.tv/en/porno-filmy/studios/daring/'
empire_beasil = 'http://sex-empire.tv/en/porno-filmy/studios/brasileirinhas/'


def get_request(page):
    return requests.get(page, headers=headers, cookies=cookies).text


def get_soup(page):
    return BeautifulSoup(get_request(page), 'html.parser')


def empire_get_request(_url):
    return requests.get(_url, headers=empire_headers, cookies=empire_cookies).text


def empire_get_soup(_url):
    return BeautifulSoup(get_request(_url), 'html.parser')


def aes(txt):

    key = binascii.unhexlify('0123456789abcdef0123456789abcdef')
    iv = binascii.unhexlify('abcdef9876543210abcdef9876543210')
    aes = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
    return base64.b64encode(aes.feed(txt) + aes.feed()).decode()


def add_dir(name, url, mode, icon, fanart, description, page='', foldername='', addcontext=False, isFolder=True):
    u = sys.argv[0]+'?name='+quote_plus(name)+'&url='+quote_plus(url)+'&mode='+quote_plus(mode)+'&icon='+quote_plus(
        icon) + '&fanart='+quote_plus(fanart)+'&description='+quote_plus(description)+'&page='+str(page)+'&foldername='+quote_plus(foldername)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'fanart': fanart, 'icon': icon, 'thumb': icon, 'poster': icon})
    liz.setInfo(type='video', infoLabels={'title': name, 'plot': description})
    if addcontext:
        contextMenu = []
        liz.addContextMenuItems(contextMenu)
    xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)


# get Categories
def get_categories(name, url, icon, fanart, description, foldername,  page):
    xbmcplugin.setPluginCategory(handle, foldername)
    xbmcplugin.setContent(handle, 'tvshows')
    soup = get_soup(url)
    item_list = item_list = soup.find_all('div', {'class': 'th-item2'})
    for item in item_list:
        name = item.find('div', {'class': 'th-title'}).text.strip()
        link = item.find('a', {'class': 'th-in'})['href']
        icon = base_url+item.img['data-src']
        add_dir(name, link, 'season_cat', icon, '', '', '', isFolder=True)

        # break
        # add_dir('Next Page', url, 'shows_list', '', '', 'Next Page', foldername=foldername, page=page, isFolder=False)


def empire_get_categories(name, url, icon, fanart, description, foldername,  page):
    xbmcplugin.setPluginCategory(handle, foldername)
    xbmcplugin.setContent(handle, 'empire')
    soup = empire_get_soup(url)
    item_list = item_list = soup.find_all('div', {'class': 'short-col nl nl2'})
    for item in item_list:
        name = item.find('a', {'class': 'th-title'}).text.strip()
        link = item.find('a', {'class': 'th-title'})['href']
        icon = 'http://sex-empire.tv'+item.img['data-src']
        add_dir(name, link, 'empire_season_cat',
                icon, '', '', '', isFolder=True)

# get_video list for each categories


def get_video_list(name, url, icon, description):
    soup = get_soup(url)
    item_list = soup.find_all('div', {'class': 'th-item'})
    for item in item_list:
        name = item.find('div', {'class': 'th-title'}).text.strip()
        link = item.find('a', {'class': 'th-in'})['href']
        icon = base_url+item.img['data-src']
        add_dir(name, link, 'episodes', icon, '', '', '', isFolder=False)

    for name, url in next_pag(url):
        try:
            add_dir(name, url, 'season_cat', '', '', '')
        except:
            break

    xbmcplugin.endOfDirectory(handle)
    # for name, url in next_pag(url):
    #add_dir(next_pag(name), next_pag(url), 'season_cat', '', '', '')


def empire_get_video_list(name, url, icon, description):
    soup = empire_get_soup(url)
    item_list = soup.find_all('div', {'class': 'short nl nl2'})
    for item in item_list:
        name = item.find('a', {'class': 'th-title'}).text.strip()
        link = item.find('a', {'class': 'th-title'})['href']
        icon = empire_base+item.img['data-src']
        add_dir(name, link, 'empire_episodes',
                icon, '', '', '', isFolder=False)

    for name, url in empire_next_pag(url):
        try:
            add_dir(name, url, 'empire_season_cat', '', '', '')
        except:
            break

    xbmcplugin.endOfDirectory(handle)
# get episode video link


def get_video(name, url, icon, description):
    # item_list = []
    #soup = get_soup(url)
    item_list = get_soup(url)
    ui = item_list.find('iframe')['src'].split('/')[6]
    link_post = 'https://api.svh-api.ch/api/v4/player'
    description = item_list.find(
        'div', {'class': 'fdesc clearfix fsubtitle'}).text
    data = {
        "idi": ui,
        "token": aes(ui),
    }

    response = requests.post(
        link_post, headers=post_headers, data=json.dumps(data), verify=False).text

    json_data = json.loads(response)
    name = ''
    link = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response)[0]
    # if link.startswith('[360p]'):
    #link = json_data['file'][6:]
    # else:
    #link = json_data['file']

    icon = json_data['poster']

    # link = get_multilink(item_list)
    play_video(name, link, icon, description)


def empire_get_video(name, url, icon, description):
    #item_list = []
    soup = empire_get_soup(url)
    description = soup.find('div', class_='fdesc').text.strip()
    item_list = re.findall(
        '(?<=#2Ly9wcm90b252aWRlby50by9pZnJhbWUv)(.*?)(?=vP3Bqc2Zy)', empire_get_request(url))[0]
    de = base64.b64decode(item_list+"=")
    ui = de.decode('utf-8')
    link_post = 'https://api.svh-api.ch/api/v4/player'
    # description = item_list.find(
    # 'div', {'class': 'fdesc clearfix fsubtitle'}).text
    data = {
        "idi": ui,
        "token": aes(ui),
    }

    response = requests.post(
        link_post, headers=post_headers, data=json.dumps(data), verify=False).text

    json_data = json.loads(response)
    name = ''
    link = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response)[0]
    # if link.startswith('[360p]'):
    #link = json_data['file'][6:]
    # else:
    #link = json_data['file']

    icon = json_data['poster']

    # link = get_multilink(item_list)
    play_video(name, link, icon, description)


def get_multilink(urls):
    labels = []
    links = []
    for url in urls:
        labels.append(url[0])
        links.append(url[1])
    if len(links) > 1:
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Choose a Link', labels)
        if ret < 0:
            return
        else:
            return links[ret]
    elif len(links) == 1:
        return links[0]
    else:
        return


# second way for handle pagination
""" def pagination(url):
    item_list = []
    for page in get_soup(url).select('a[class="button mobile-hide pagi-btn"]'):
        item_list.append([page.text.strip(), base_url+page['href']])
    return item_list


def next_page(url):
    item_list = []
    soup = get_soup(url)
    string_list = str(soup)
    nextp = soup.find_all('a', {'class': 'button mobile-pagi pagi-btn'})
    for item in nextp:
        link = "https://www.hqporner.com"+item['href']
        name = item.text
        item_list.append([name, link])
        return item_list """


def next_pag(url):
    item_list = []
    res = get_request(url).replace("<!--", "").replace("-->", "")
    soup = BeautifulSoup(res, 'html.parser')
    try:
        url = soup.find('div', {'class': 'pnext'}).a['href']
        #name = 'Next Page'
    except:
        url = None
    name = 'Next Page'
    link = url
    item_list.append([name, link])
    return item_list


def empire_next_pag(url):
    item_list = []
    soup = empire_get_soup(url)
    try:
        url = soup.find('span', {'class': 'pnext'}).a['href']
        #name = 'Next Page'
    except:
        url = None

    name = 'Next Page'
    link = url
    item_list.append([name, link])
    return item_list


def play_video(name, url, icon, description):
    liz = xbmcgui.ListItem(name)
    liz.setInfo('video', {'title': name, 'plot': description})
    liz.setArt({'thumb': icon, 'icon': icon})
    xbmc.Player().play(url, liz)


def main_menu():
    xbmcplugin.setPluginCategory(handle, 'Main Menu')
    add_dir('Manoto', '', 'shows_main', '', '',
            'Manoto TV ', isFolder=True)
    add_dir('Empire', '', 'empire_shows_main', '', '',
            'Empire TV', isFolder=True)
    # add_dir('Soup Trailers', '', 'shows_main', '',
    # '', 'Soup Trailers', isFolder=True)
    # add_dir('Wallpaper', '', 'shows_main', '',
    # '', 'HD Wallpaper', isFolder=True)


def shows_main():
    xbmcplugin.setPluginCategory(handle, 'TV Shows')
    add_dir('Collections', base_categories, 'shows_list', '', '',
            'Collections', foldername='Collections', isFolder=True)
    add_dir('Top 100', base_top, 'season_cat', '', '',
            'Top 100', foldername='Top 100', isFolder=True)
    add_dir('Latest Videos', base_new, 'season_cat', '', '',
            'Latest Videos', foldername='Latest Videos', isFolder=True)
    add_dir('USA', base_usa, 'season_cat', '', '',
            'USA', foldername='USA', isFolder=True)
    add_dir('Italy', base_italy, 'season_cat', '', '',
            'Italy', foldername='Italy', isFolder=True)
    add_dir('France', base_france, 'season_cat', '', '',
            'France', foldername='France', isFolder=True)
    add_dir('Spain', base_spain, 'season_cat', '', '',
            'Spain', foldername='Spain', isFolder=True)
    add_dir('Europe', base_eroupe, 'season_cat', '', '',
            'Europe', foldername='Europe', isFolder=True)
    add_dir('Marc Dorcel', base_dorcel, 'season_cat', '', '',
            'Marc Dorcel', foldername='Marc Dorcel', isFolder=True)
    add_dir('Wicked Pictures', base_wicked, 'season_cat', '', '',
            'Wicked Pictures', foldername='Wicked Pictures', isFolder=True)
    add_dir('Digital Playground', base_digital, 'season_cat', '', '',
            'Digital Playground', foldername='Digital Playground', isFolder=True)
    add_dir('Private', base_private, 'season_cat', '', '',
            'Private', foldername='Private', isFolder=True)
    add_dir('Mario Salieri', base_mario, 'season_cat', '', '',
            'Mario Salieri', foldername='Mario Salieri', isFolder=True)
    add_dir('Classic', base_classic, 'season_cat', '', '',
            'Classic', foldername='Classic', isFolder=True)
    add_dir('Parodies', base_paradoies, 'season_cat', '', '',
            'Parodies', foldername='Parodies', isFolder=True)
    add_dir('Scenes', base_scenes, 'season_cat', '', '',
            'Scenes', foldername='Scenes', isFolder=True)


def empire_show_main():
    xbmcplugin.setPluginCategory(handle, 'Empire')
    add_dir('Collections', empire_categories, 'empire_shows_list', '', '',
            'Collections', foldername='Collections', isFolder=True)
    add_dir('Top 100', empire_top, 'empire_season_cat', '', '',
            'Top 100', foldername='Top 100', isFolder=True)
    add_dir('Full HD', empire_fullHD, 'empire_season_cat', '', '',
            'Full HD', foldername='Full HD', isFolder=True)
    add_dir('Latest Videos', empre_latest, 'empire_season_cat', '', '',
            'Latest Videos', foldername='Latest Videos', isFolder=True)
    add_dir('USA', empire_usa, 'empire_season_cat', '', '',
            'USA', foldername='USA', isFolder=True)
    add_dir('Italy', empire_italy, 'empire_season_cat', '', '',
            'Italy', foldername='Italy', isFolder=True)
    add_dir('France', empire_france, 'empire_season_cat', '', '',
            'France', foldername='France', isFolder=True)
    add_dir('Spain', empire_spain, 'empire_season_cat', '', '',
            'Spain', foldername='Spain', isFolder=True)
    add_dir('Europe', empire_eroupe, 'empire_season_cat', '', '',
            'Europe', foldername='Europe', isFolder=True)
    add_dir('Marc Dorcel', empire_dorcel, 'empire_season_cat', '', '',
            'Marc Dorcel', foldername='Marc Dorcel', isFolder=True)
    add_dir('Wicked Pictures', empire_wicked, 'empire_season_cat', '', '',
            'Wicked Pictures', foldername='Wicked Pictures', isFolder=True)
    add_dir('Digital Playground', empire_digital, 'empire_season_cat', '', '',
            'Digital Playground', foldername='Digital Playground', isFolder=True)
    add_dir('Private', empire_private, 'empire_season_cat', '', '',
            'Private', foldername='Private', isFolder=True)
    add_dir('Mario Salieri', empire_mario, 'empire_season_cat', '', '',
            'Mario Salieri', foldername='Mario Salieri', isFolder=True)
    add_dir('Hustler', empire_hustler, 'empire_season_cat', '', '',
            'Hustler', foldername='Hustler', isFolder=True)
    add_dir('New Sensations', empire_sensation, 'empire_season_cat', '', '',
            'New Sensations', foldername='New Sensations', isFolder=True)
    add_dir('Pure Taboo', empire_tabo, 'empire_season_cat', '', '',
            'Pure Taboo', foldername='Pure Taboo', isFolder=True)
    add_dir('Daring', empire_daring, 'empire_season_cat', '', '',
            'Daring', foldername='Daring', isFolder=True)
    add_dir('Brasileirinhas', empire_beasil, 'empire_season_cat', '', '',
            'Brasileirinhas', foldername='Brasileirinhas', isFolder=True)
    add_dir('Classic', empire_classic, 'empire_season_cat', '', '',
            'Classic', foldername='Classic', isFolder=True)
    add_dir('Parodies', empire_paradoies, 'empire_season_cat', '', '',
            'Parodies', foldername='Parodies', isFolder=True)
    add_dir('Scenes', empire_scenes, 'empire_season_cat', '', '',
            'Scenes', foldername='Scenes', isFolder=True)


def router():

    #---System Arguments---#

    p = dict(parse_qsl(sys.argv[2][1:]))
    mode = p.get('mode', 'main_menu')
    name = p.get('name', '')
    url = p.get('url', '')
    icon = p.get('icon', '')
    fanart = p.get('fanart', '')
    description = p.get('description', '')
    page = p.get('page', '')
    foldername = p.get('foldername', '')

    #---Modes---#

    if mode == 'main_menu':
        main_menu()

    elif mode == 'shows_main':
        shows_main()

    elif mode == 'empire_shows_main':
        empire_show_main()

    elif mode == 'shows_list':
        get_categories(name, url, icon, fanart, description, foldername, page)

    elif mode == 'empire_shows_list':
        empire_get_categories(name, url, icon, fanart,
                              description, foldername, page)

    elif mode == 'season_cat':
        get_video_list(name, url, icon, description)

    elif mode == 'empire_season_cat':
        empire_get_video_list(name, url, icon, description)

    elif mode == 'episodes':
        get_video(name, url, icon, description)

    elif mode == 'empire_episodes':
        empire_get_video(name, url, icon, description)

    elif mode == 'play_video':
        play_video(name, url, icon, description)

    #---End the Directory---#

    xbmcplugin.endOfDirectory(handle)

#---Addon Begins Here---#


if __name__ == '__main__':
    router()
