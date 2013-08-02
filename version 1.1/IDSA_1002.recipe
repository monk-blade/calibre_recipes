class BasicUserRecipe1374241209(AutomaticNewsRecipe):
    title          = u'IDSA'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True
	description = u'Indian Defence Studies and Analysis web site ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'news, blog'

    # Set publisher and publication type.
    publisher = 'IDSA'
    publication_type = 'blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True , 'search_replace': '[["Views expressed are of the author and do not necessarily reflect the views of the IDSA or of the Government of India.", ""]]' }

    feeds          = [(u'Current News', u'http://idsa.in/rss.xml')]
