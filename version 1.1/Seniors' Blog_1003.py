from calibre.utils.magick import Image
class BasicUserRecipe1374243149(AutomaticNewsRecipe):
    title          = u"Seniors' Blog"
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True
	description = u'Senior IAS officers Blog'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'ias, blog'

    # Set publisher and publication type.
    publisher = 'swapsusias'
    publication_type = 'blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    feeds          = [(u'Current Feeds', u'http://swapsushias.blogspot.com/feeds/posts/default?alt=rss')]
    def postprocess_html(self, soup, first):
        #process all the images
        for tag in soup.findAll(lambda tag: tag.name.lower()=='img' and tag.has_key('src')):
            iurl = tag['src']
            img = Image()
            img.open(iurl)
            if img < 0:
                raise RuntimeError('Out of memory')
            img.type = "GrayscaleType"
            img.save(iurl)
        return soup