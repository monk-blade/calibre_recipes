from calibre.constants import config_dir, CONFIG_DIR_MODE
import os, os.path, urllib
from hashlib import md5

class OnlyLatestRecipe(BasicNewsRecipe):
    title          = u'The Hindu'
    oldest_article = 2
    max_articles_per_feed = 1000
    auto_cleanup = True
    masthead_url = 'http://www.thehindu.com/template/1-0-1/gfx/logo.jpg'
    description = u'The Hindu newspaper ebook'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set category.
    category = 'news'

    # Set publisher and publication type.
    publisher = 'The Hindu'
    publication_type = 'newspaper'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True , 'search_replace': '[["<img height=\\"21\\" width=\\"43\\" src=\\"images/00006.jpg\\".*/>", ""]]'}

    feeds          = [(u'National', u'http://www.thehindu.com/news/national/?service=rss'), (u'International', u'http://www.thehindu.com/news/international/?service=rss'), (u'Lead', u'http://www.thehindu.com/opinion/lead/?service=rss'), (u'Columns', u'http://www.thehindu.com/opinion/columns/?service=rss'), (u'Editorial', u'http://www.thehindu.com/opinion/editorial/?service=rss'), (u'Letters', u'http://www.thehindu.com/opinion/letters/?service=rss'), (u'Op-Ed', u'http://www.thehindu.com/opinion/op-ed/?service=rss'), (u"Readers' Editor", u'http://www.thehindu.com/opinion/Readers-Editor/?service=rss'), (u'Energy & Environment', u'http://www.thehindu.com/sci-tech/energy-and-environment/?service=rss'), (u'Health', u'http://www.thehindu.com/sci-tech/health/?service=rss'), (u'Education', u'http://www.thehindu.com/features/education/?service=rss'), (u'Science', u'http://www.thehindu.com/sci-tech/science/?service=rss'), (u'Technology', u'http://www.thehindu.com/sci-tech/technology/?service=rss'), (u'Economy', u'http://www.thehindu.com/business/Economy/?service=rss'), (u'Sports', u'http://www.thehindu.com/sport/?service=rss'), (u'Industry', u'http://www.thehindu.com/business/Industry/?service=rss'), (u'Friday Feast', u'http://www.thehindu.com/features/friday-review/?service=rss')]   

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
