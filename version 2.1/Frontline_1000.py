from calibre.constants import config_dir, CONFIG_DIR_MODE
import os, os.path, urllib
from hashlib import md5

class OnlyLatestRecipe(BasicNewsRecipe):
    title          = u'Frontline'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True
    masthead_url = 'http://www.frontline.in/template/1-0-1/gfx/fl_logo.jpg'
    description = u'Frontline magazine ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'news, sport, blog'

    # Set publisher and publication type.
    publisher = 'Frontline'
    publication_type = 'magazine'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True }

    feeds          = [(u'Home', u'http://www.frontline.in/?service=rss')]

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
