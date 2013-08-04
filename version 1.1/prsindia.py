__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
prsindia.org
'''

class BasicUserRecipe1374240928(AutomaticNewsRecipe):
    title          = u'PRS India'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True

    description = u'PRS India Blog website ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'analysis'

    # Set publisher and publication type.
    publisher = 'PRSindia'
    publication_type = 'blog'
    masthead_url = 'http://ubuntuone.com/6WdjsuwJA7OX5uXRVFbGOb'
    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    feeds          = [(u'Recent Articles', u'http://www.prsindia.org/theprsblog/?feed=rss2')]
