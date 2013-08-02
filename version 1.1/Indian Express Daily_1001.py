class AdvancedUserRecipe1365325384(BasicNewsRecipe):
    title          = u'Indian Express Daily'
    oldest_article = 2
    max_articles_per_feed = 100
    auto_cleanup = True
	description = u'Indian Express Column's ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'news'

    # Set publisher and publication type.
    publisher = 'Indian Express'
    publication_type = 'newspaper'

    # Disable stylesheets from site.
    no_stylesheets = True
    remove_tags = [dict(name='div', attrs={'class':'termstoolbox'}), dict(name='span', attrs={'class':'tnc'})]
    encoding = None
    remove_javascript = True
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True , 'search_replace': '[["TERMS OF USE: .*.", ""], ["express@expressindia.com", ""]]' }
    feeds = [(u'Editorials', u'http://syndication.indianexpress.com/rss/35/editorials.xml'), (u'Columns', u'http://syndication.indianexpress.com/rss/1295/express-columns.xml'), (u'Economy', u'http://syndication.indianexpress.com/rss/794/economy.xml'), (u'Op-Ed', u'http://syndication.indianexpress.com/rss/36/oped.xml'), (u'Science & Technology', u'http://syndication.indianexpress.com/rss/698/science---technology.xml'), (u'Climate Change', u'http://syndication.indianexpress.com/rss/912/climate-change.xml'), (u'ET-Environment', u'http://economictimes.indiatimes.com/rssfeeds/2647180.cms'), (u'Letters', u'http://syndication.indianexpress.com/rss/40/letters-to-editor.xml'), (u'Art & Culture', u'http://syndication.indianexpress.com/rss/1229/art---culture.xml')]

    def print_version(self, url):
        return url+'/0'

