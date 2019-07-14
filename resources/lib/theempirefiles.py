import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup)
    return soup

get_soup("https://toppodcast.com/podcast_feeds/empire-files/")


def get_playable_podcast(soup):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all('article'):
        
        try:        
            link = content.find('divclass=player')
            link = link.get('audiosrc')
            print "\n\nLink: ", link

            title = content.find('class=title')
            title = title.get_text()

            desc = content.find('class="addReadMore showlesscontent')
            desc = desc.get_text()

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
                'desc': desc,
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast(playable_podcast):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': "https://toppodcast.com/wp-content/uploads/2019/07/52242-600x600bb-85-300x300.png",
            'path': podcast['url'],
            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast1(soup):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all('item', limit=1):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

            desc = content.find('description')
            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
                'desc': desc,
                'thumbnail': "http://static.libsyn.com/p/assets/7/2/8/0/72802e4963645d76/DPS_Podcast_new.jpg"
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_past_episodes(soup2):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup2.find_all('article'):
        
        try:        
            link = content.find('source')
            link = link.get('src')
            print "\n\nLink: ", link

            title = content.find('h5')
            title = title.get_text()

#            desc = content.find('On the Show')
#            desc = desc.get_text('p')

#            thumbnail = content.find('h4')
#            thumbnail = thumbnail.get()

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://davidpakman.com/wp-content/uploads/2016/03/cropped-tdps-icon-300x300.png"
        }
        
        subjects.append(item) 
    
    return subjects


def compile_past_episodes(past_episodes):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in past_episodes:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items
