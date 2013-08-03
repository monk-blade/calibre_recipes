class AdvancedUserRecipe1365325360(BasicNewsRecipe):
    title          = u'Indian Express Columns'
    oldest_article = 21
    max_articles_per_feed = 100
    auto_cleanup = True
    masthead_url = 'http://static.indianexpress.com/frontend/iep/images/images_new2013/logo.jpg'
	description = u'Indian Express Column\'s ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'news, blog'

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
    feeds          = [(u'C. Raja Mohan (Diplomacy)', u'http://syndication.indianexpress.com/rss/columnist/crajamohan.xml'), (u'Sunday Stories', u'http://syndication.indianexpress.com/rss/723/sunday-stories.xml')]

    def print_version(self, url):
        return url+'/0'

