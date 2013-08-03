class AdvancedUserRecipe1365325651(BasicNewsRecipe):
    title          = u'The Hindu'
    oldest_article = 2
    max_articles_per_feed = 100
    auto_cleanup = True
    masthead_url = 'http://www.thehindu.com/template/1-0-1/gfx/logo.jpg'
    description = u'The Hindu newspaper ebook'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'news'

    # Set publisher and publication type.
    publisher = 'The Hindu'
    publication_type = 'newspaper'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True , 'search_replace': '[["<img height=\\"21\\" width=\\"43\\" src=\\"images/00006.jpg\\".*/>", ""]]'}
    feeds = [(u'National', u'http://www.thehindu.com/news/national/?service=rss'), (u'International', u'http://www.thehindu.com/news/international/?service=rss'), (u'Lead', u'http://www.thehindu.com/opinion/lead/?service=rss'), (u'Columns', u'http://www.thehindu.com/opinion/columns/?service=rss'), (u'Editorial', u'http://www.thehindu.com/opinion/editorial/?service=rss'), (u'Letters', u'http://www.thehindu.com/opinion/letters/?service=rss'), (u'Op-Ed', u'http://www.thehindu.com/opinion/op-ed/?service=rss'), (u"Readers' Editor", u'http://www.thehindu.com/opinion/Readers-Editor/?service=rss'), (u'Energy & Environment', u'http://www.thehindu.com/sci-tech/energy-and-environment/?service=rss'), (u'Medicine & Research', u'http://www.thehindu.com/sci-tech/health/medicine-and-research/?service=rss'), (u'Policy & Issues', u'http://www.thehindu.com/sci-tech/health/policy-and-issues/?service=rss'), (u'Education', u'http://www.thehindu.com/features/education/?service=rss'), (u'Science', u'http://www.thehindu.com/sci-tech/science/?service=rss'), (u'Technology', u'http://www.thehindu.com/sci-tech/technology/?service=rss'), (u'Economy', u'http://www.thehindu.com/business/Economy/?service=rss'), (u'Industry', u'http://www.thehindu.com/business/Industry/?service=rss'), (u'Friday Feast', u'http://www.thehindu.com/features/friday-review/?service=rss')]

