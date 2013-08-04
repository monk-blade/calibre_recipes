__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
indianexpress.com
'''

from calibre.constants import config_dir, CONFIG_DIR_MODE
import os, os.path, urllib
from hashlib import md5

class OnlyLatestRecipe(BasicNewsRecipe):
    title          = u'Indian Express'
    oldest_article = 2
    max_articles_per_feed = 1000
    auto_cleanup = True
    masthead_url = 'http://static.indianexpress.com/frontend/iep/images/images_new2013/logo.jpg'
    description = u'Indian Express Newspaper ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set category.
    category = 'news'

    # Set publisher and publication type.
    publisher = 'Indian Express'
    publication_type = 'newspaper'

    # Disable stylesheets from site.
    no_stylesheets = True
    remove_tags = [dict(name='div', attrs={'class':'termstoolbox'}), dict(name='span', attrs={'class':'tnc'})]
    encoding = None
    remove_javascript = True
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True , 'search_replace': '[["TERMS OF USE: .*.", ""], ["express@expressindia.com", ""]]' }

    feeds          = [(u'Editorials', u'http://syndication.indianexpress.com/rss/35/editorials.xml'), (u'Columns', u'http://syndication.indianexpress.com/rss/1295/express-columns.xml'), (u'Economy', u'http://syndication.indianexpress.com/rss/794/economy.xml'), (u'Op-Ed', u'http://syndication.indianexpress.com/rss/36/oped.xml'), (u'Science & Technology', u'http://syndication.indianexpress.com/rss/698/science---technology.xml'), (u'Climate Change', u'http://syndication.indianexpress.com/rss/912/climate-change.xml'), (u'ET-Environment', u'http://economictimes.indiatimes.com/rssfeeds/2647180.cms'), (u'Letters', u'http://syndication.indianexpress.com/rss/40/letters-to-editor.xml'), (u'Art & Culture', u'http://syndication.indianexpress.com/rss/1229/art---culture.xml'), (u'C. Raja Mohan (Diplomacy)', u'http://syndication.indianexpress.com/rss/columnist/crajamohan.xml'), (u'Sunday Stories', u'http://syndication.indianexpress.com/rss/723/sunday-stories.xml')]

    def print_version(self, url):
        return url+'/0'

    def parse_feeds(self):
        recipe_dir = os.path.join(config_dir,'recipes')
        hash_dir = os.path.join(recipe_dir,'recipe_storage')
        feed_dir = os.path.join(hash_dir,self.title.encode('utf-8').replace('/',':'))
        if not os.path.isdir(feed_dir):
            os.makedirs(feed_dir,mode=CONFIG_DIR_MODE)

        feeds = BasicNewsRecipe.parse_feeds(self)

        for feed in feeds:
            feed_hash = urllib.quote(feed.title.encode('utf-8'),safe='')
            feed_fn = os.path.join(feed_dir,feed_hash)

            past_items = set()
            if os.path.exists(feed_fn):
               with file(feed_fn) as f:
                   for h in f:
                       past_items.add(h.strip())
            cur_items = set()
            for article in feed.articles[:]:
                item_hash = md5()
                if article.content: item_hash.update(article.content.encode('utf-8'))
                if article.summary: item_hash.update(article.summary.encode('utf-8'))
                item_hash = item_hash.hexdigest()
                if article.url:
                    item_hash = article.url + ':' + item_hash
                cur_items.add(item_hash)
                if item_hash in past_items:
                    feed.articles.remove(article)
            with file(feed_fn,'w') as f:
                for h in cur_items:
                    f.write(h+'\n')

        remove = [f for f in feeds if len(f) == 0 and
                self.remove_empty_feeds]
        for f in remove:
            feeds.remove(f)

        return feeds
