import scrapy


class OrangeSpider(scrapy.Spider):
    name = 'orange'
    allowed_domains = ['www.mozilla.org']
    start_urls = ['http://www.mozilla.org/']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield
                scrapy.Request(response.urljoin(next_page), callback=self.parse)

