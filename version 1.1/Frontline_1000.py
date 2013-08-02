class BasicUserRecipe1374243421(AutomaticNewsRecipe):
    title          = u'Frontline'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True
    description = u'Frontline magazine ebook created using rss feeds.'
    masthead_url = 'http://www.frontline.in/template/1-0-1/gfx/fl_logo.jpg'
    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'news, sport, blog'

    # Set publisher and publication type.
    publisher = 'Frontline'
    publication_type = 'magazine'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True }

    feeds          = [(u'Home', u'http://www.frontline.in/?service=rss')]
