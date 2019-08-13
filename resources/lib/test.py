import requests
import re
from bs4 import BeautifulSoup

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
    
    print subjects
