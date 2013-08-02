class AdvancedUserRecipe1365341701(BasicNewsRecipe):
    title          = u'PIB'
    oldest_article = 1000000
    max_articles_per_feed = 25
    auto_cleanup = False
    description = u'Press Information Beuro Ebook'
    masthead_url = 'http://pib.nic.in/newsite/image/pibimage.jpg'
    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'news, current-affairs'

    # Set publisher and publication type.
    publisher = 'PIB'
    publication_type = 'blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'remove_paragraph_spacing': True, 'remove_paragraph_spacing_indent_size': 1.2, 'smarten_punctuation' : True , 'search_replace': '[["\\u00c2", ""]]'}

    feeds          = [(u'Current Feeds', u'http://pib.nic.in/newsite/rssenglish_fea.aspx')]
    keep_only_tags = [dict(name='div', attrs={'class':'contentdiv'})]
    preprocess_regexps = [
   (re.compile(r'\(PIB Features.*</body>', re.DOTALL|re.IGNORECASE),
    lambda match: '</body>'),
]
    extra_css = ' #title { font-family: verdana, helvetica, sans-serif; }     #title { font-weight: bold; font-size: 150%;}'