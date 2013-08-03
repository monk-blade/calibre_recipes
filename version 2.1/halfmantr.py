__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
halfmantr.com
'''

import re
from calibre import strftime
from calibre.web.feeds.news import BasicNewsRecipe
from calibre.constants import config_dir, CONFIG_DIR_MODE
import os, os.path, urllib
from hashlib import md5

class Frontlineonnet(BasicNewsRecipe):
    title                = 'Halfmantr'
    __author__           = 'Arpan Chavda'
    description          = "UPSC Preparation Blog"
    publisher            = 'Halfmantr'
    category             = 'upsc'
    no_stylesheets       = True
#    max_articles_per_feed = 1
    auto_cleanup = True
    INDEX                = 'http://www.halfmantr.com/'
    use_embedded_content = False
    encoding             = 'utf-8'
    language             = 'en_IN'
    publication_type     = 'magazine'
    #masthead_url         = 'http://www.sportstaronnet.com/ss_weekly.jpg'
    extra_css            = """
                              body{font-family: Verdana,Arial,Helvetica,sans-serif}
                              img{margin-top:0.5em; margin-bottom: 0.7em; display: block}
                           """

    conversion_options = {
                          'comment'          : description
                        , 'tags'             : category
                        , 'publisher'        : publisher
                        , 'language'         : language
                        }

    preprocess_regexps = [
                           (re.compile(r'.*?<base', re.DOTALL|re.IGNORECASE),lambda match: '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"><html dir="ltr" xml:lang="en-IN"><head><title>title</title><base')
                          ,(re.compile(r'<base .*?>', re.DOTALL|re.IGNORECASE),lambda match: '</head><body>')
                          ,(re.compile(r'<byline>', re.DOTALL|re.IGNORECASE),lambda match: '<div class="byline">')
                          ,(re.compile(r'</byline>', re.DOTALL|re.IGNORECASE),lambda match: '</div>')
                          ,(re.compile(r'<center>', re.DOTALL|re.IGNORECASE),lambda match: '<div class="ctr">')
                          ,(re.compile(r'</center>', re.DOTALL|re.IGNORECASE),lambda match: '</div>')
                          
                         ]
    auto_cleanup_keep = '//div[@class="newsitem_text"]'
    #keep_only_tags = [dict(name='div', attrs={'class':'newsitem_text'})]
    def parse_index(self):
        articles = []
        feeds = []
        soup = self.index_to_soup(self.INDEX)
        for feed_link in soup.findAll("a" , "latestnews_menu"):
            
                url   = self.INDEX + feed_link['href']
                title = self.tag_to_string(feed_link)
                date  = strftime(self.timefmt)
                articles.append({
                                  'title'      :title
                                 ,'date'       :date
                                 ,'url'        :url
                                 ,'description':''
                                })
        if articles:
            feeds.append(('Latest Articles', articles))
        return feeds
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