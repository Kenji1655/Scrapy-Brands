import scrapy

class BrandSortedSpider(scrapy.Spider):
    name = 'brandsorted'
    allowed_domains = ['rankingthebrands.com']
    start_urls = ['https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=A']

    def parse(self, response):
        for brands in response.css('div.brandLine'):
            yield {
                'brand': brands.css('span.rankingName::text').get(),
            }

        letter_links = response.css('div.abcbg a::attr(href)').getall()
        letter_links = sorted(set(letter_links))  
        letter_links = [response.urljoin(link) for link in letter_links]
    
        if response.url in letter_links:
            current_index = letter_links.index(response.url)
            if current_index + 1 < len(letter_links):  
                next_page = letter_links[current_index + 1]
                yield response.follow(next_page, callback=self.parse)
