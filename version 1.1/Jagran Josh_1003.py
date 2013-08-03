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

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True }

    feeds          = [(u'Current Affairs', u'http://www.jagranjosh.com/rss/josh/current_affairs.xml')]
