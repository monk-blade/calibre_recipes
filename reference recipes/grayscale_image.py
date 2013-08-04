from calibre.utils.magick import Image
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
