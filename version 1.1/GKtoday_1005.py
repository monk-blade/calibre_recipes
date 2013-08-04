__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
gktoday.in
'''

class BasicUserRecipe1374243904(AutomaticNewsRecipe):
    title          = u'GKtoday'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True

	description = u'GKToday.in web site ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'quiz, current-affairs'

    # Set publisher and publication type.
    publisher = 'GKToday.in'
    publication_type = 'blog'
    masthead_url = 'http://www.gktoday.in/wp-content/themes/Ocean/images/logo_placement.gif'
    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True , 'search_replace': '[["Show Answer", ""], ["Download article as PDF", ""]]'}
    feeds          = [(u'Home', u'http://feeds.feedburner.com/GeneralKnowledgeToday')]
