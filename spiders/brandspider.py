import scrapy

class BrandSpider(scrapy.Spider):
    name = 'brand'
    start_urls = ['https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=A']

    def parse(self, response):
        # Extraindo todas as marcas da página atual
        for brands in response.css('div.brandLine'):
            yield {
                'brand': brands.css('span.rankingName::text').get(),
            }

        # Pegando todos os links das letras A-Z
        next_pages = response.css('div.abcbg a::attr(href)').getall()
        
        # Seguindo cada link separadamente
        for next_page in next_pages:
            yield response.follow(next_page, callback=self.parse)
