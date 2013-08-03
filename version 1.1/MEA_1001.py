class BasicUserRecipe1374240928(AutomaticNewsRecipe):
    title          = u'Ministry of External Affairs'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True

    description = u'Ministry of External Affairs website ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'news'

    # Set publisher and publication type.
    publisher = 'MEA'
    publication_type = 'blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    feeds          = [(u'In Focus News', u'http://www.mea.gov.in/Portal/XML/In_Focus_Article_1.xml')]
