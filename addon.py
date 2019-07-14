from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theempirefiles

plugin = Plugin()

URL = "https://toppodcast.com/podcast_feeds/empire-files/"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://toppodcast.com/wp-content/uploads/2019/07/52242-600x600bb-85-300x300.png"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://toppodcast.com/wp-content/uploads/2019/07/52242-600x600bb-85-300x300.png"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = theempirefiles.get_soup(URL)
    
    playable_podcast = theempirefiles.get_playable_podcast(soup)
    
    items = theempirefiles.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = theempirefiles.get_soup(URL)
    
    playable_podcast1 = theempirefiles.get_playable_podcast1(soup)
    
    items = theempirefiles.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
