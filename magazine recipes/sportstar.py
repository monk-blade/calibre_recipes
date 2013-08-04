__license__   = 'GPL v3'
__copyright__ = '2013, Arpan Chavda <arpanchavdaeng at gmail.com>'
'''
sportstaronnet.com
'''

import re
from calibre import strftime
from calibre.web.feeds.news import BasicNewsRecipe

class Frontlineonnet(BasicNewsRecipe):
    title                = 'Sportstar'
    __author__           = 'Arpan Chavda'
    description          = "India's sport magazine"
    publisher            = 'Sportstar'
    category             = 'news, sports, India'
    no_stylesheets       = True
    INDEX                = 'http://www.sportstaronnet.com/'
    use_embedded_content = False
    encoding             = 'utf-8'
    language             = 'en_IN'
    publication_type     = 'magazine'
    masthead_url         = 'http://www.sportstaronnet.com/ss_weekly.jpg'
    extra_css            = """
                              body{font-family: Verdana,Arial,Helvetica,sans-serif}
                              img{margin-top:0.5em; margin-bottom: 0.7em; display: block}
                           """

    conversion_options = {
                          'comment'          : description
                        , 'tags'             : category
                        , 'publisher'        : publisher
                        , 'language'         : language
                        ,'search_replace': '[["<a.*>Back</a>", ""], ["<span.*>Vol.*</span>", ""], ["<span.*>URL.*</span>", ""]]'
                        }

    preprocess_regexps = [
                           (re.compile(r'.*?<base', re.DOTALL|re.IGNORECASE),lambda match: '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"><html dir="ltr" xml:lang="en-IN"><head><title>title</title><base')
                          ,(re.compile(r'<base .*?>', re.DOTALL|re.IGNORECASE),lambda match: '</head><body>')
                          ,(re.compile(r'<byline>', re.DOTALL|re.IGNORECASE),lambda match: '<div class="byline">')
                          ,(re.compile(r'</byline>', re.DOTALL|re.IGNORECASE),lambda match: '</div>')
                          ,(re.compile(r'<center>', re.DOTALL|re.IGNORECASE),lambda match: '<div class="ctr">')
                          ,(re.compile(r'</center>', re.DOTALL|re.IGNORECASE),lambda match: '</div>')
                         ]

    def parse_index(self):
        articles = []
        feeds = []
        soup = self.index_to_soup(self.INDEX)
        for feed_link in soup.findAll('a',href=True):
            if feed_link['href'].startswith('stories/'):
                url   = self.INDEX + feed_link['href']
                title = self.tag_to_string(feed_link)
                date  = strftime(self.timefmt)
                articles.append({
                                  'title'      :title
                                 ,'date'       :date
                                 ,'url'        :url
                                 ,'description':''
                                })
        if articles:
            feeds.append(('Frontline', articles))
        return feeds

    def print_version(self, url):
        return "http://www.hinduonnet.com/thehindu/thscrip/print.pl?prd=fline&file=" + url.rpartition('/')[2] + "&date=tss3631/&prd=tss&"

    def image_url_processor(self, baseurl, url):
        return url.replace('../images/', self.INDEX + 'images/').strip()
