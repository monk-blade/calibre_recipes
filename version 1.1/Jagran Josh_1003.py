__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
jagranjosh.in
'''

class BasicUserRecipe1365323696(AutomaticNewsRecipe):
    title          = u'Jagran Josh'
    oldest_article = 15
    max_articles_per_feed = 100
    auto_cleanup = True
	description = u'Jagran Josh web site ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'current-affairs, blog'

    # Set publisher and publication type.
    publisher = 'Jagran Josh'
    publication_type = 'blog'
    masthead_url = 'http://www.jagranjosh.com/Resources/edu2/images/jagran_josh_logo.gif'
    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    feeds          = [(u'Current Affairs', u'http://www.jagranjosh.com/rss/josh/current_affairs.xml')]
