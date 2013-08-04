__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
mrunal.org
'''

class AdvancedUserRecipe1365325396(BasicNewsRecipe):
    title          = u'Mrunal.org'
    oldest_article = 7
    max_articles_per_feed = 10000
    auto_cleanup = True
    description = u'Mrunal blog ebook created using rss feeds.'
    masthead_url = 'https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-frc1/376962_238261119628582_1219921430_n.jpg'
    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_IN'

    # Set tags.
    tags = 'blog'

    # Set publisher and publication type.
    publisher = 'Mrunal Patel'
    publication_type = 'Blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    feeds          = [(u'Current Feeds', u'http://mrunal.org/feed')]

    def print_version(self, url):
        return url+'/print'

