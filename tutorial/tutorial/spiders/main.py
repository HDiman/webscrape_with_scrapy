import scrapy
import requests

fetch('https://quotes.toscrape.com/tag/inspirational/')
fetch('https://www.imdb.com/chart/top')

fetch('https://www.reddit.com/r/funny/')
fetch('https://www.reddit.com/r/funny/hot/')


scrapy shell https://quotes.toscrape.com/tag/inspirational/
scrapy shell https://www.imdb.com/chart/top/

response.url
or
response.text

url = 'https://quotes.toscrape.com/tag/inspirational/'
fetch("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url=url, headers=header)
response = response.text
# print(response)


for author in response.css('div.quote span small ::text').getall():
    print(author)

for item in response.css('div.rpBJOHq2PR60pnwJlUyP0 div h3 ::text').getall():
    print(item)



# for author in response.css('div.quote span small').getall():
#     print(author)
#
#
# for quote_sel in response.css('.quote'):
#     quote_sel.css('.text::text').get()
#     quote_sel.css('.author::text').get()
#
#
# for film in response.css('.lister-list'):
#     film.css('.titleColumn a::text').get()
#
# for film in response.css('.lister-list .titleColumn a::text').getall():
#     print(film)
#
# for film in response.css('.lister-list'):
#     film.css('.titleColumn::text').get()
#     film.css('.titleColumn a::text').get()

# .lister-list .titleColumn

# for price in response.css('.photo-cards .list-card-price ::text').getall():
#     print(price)


# --- Block for one project ---
fetch('https://www.reddit.com/r/funny/')
response.url
response.text

# Articles
for item in response.css('h3._eYtD2XCVieq6emjKBH3m ::text').extract():
    print(item)
# Href-s
for href in response.css('a.SQnoC3ObvgnGjWt90zD9Z ::attr(href)').extract():
    print(href)
# Votes
for vote in response.css('._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo ::text').extract():
    print(vote)