__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
idsa.in
'''

class BasicUserRecipe1374241209(AutomaticNewsRecipe):
    title          = u'IDSA'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True
	description = u'Indian Defence Studies and Analysis web site ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'news, blog'

    # Set publisher and publication type.
    publisher = 'IDSA'
    publication_type = 'blog'
    masthead_url = 'http://idsa.in/themes/idsa2012/images/logo.gif'
    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True , 'search_replace': '[["Views expressed are of the author and do not necessarily reflect the views of the IDSA or of the Government of India.", ""]]' }

    feeds          = [(u'Current News', u'http://idsa.in/rss.xml')]
