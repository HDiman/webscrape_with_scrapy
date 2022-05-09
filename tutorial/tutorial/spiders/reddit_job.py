import scrapy

class RedditJobSpider(scrapy.Spider):
    name = "reddit_job"

    # where to extract the data
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/funny/']

    # how to extract to data
    def parse(self, response):
        # Articles
        for item in response.css('h3._eYtD2XCVieq6emjKBH3m ::text').extract():
            print(item)
        # Href-s
        for href in response.css('a.SQnoC3ObvgnGjWt90zD9Z ::attr(href)').extract():
            print(href)
        # Votes
        for vote in response.css('._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo ::text').extract():
            print(vote)

