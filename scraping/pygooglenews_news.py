from pygooglenews import GoogleNews
import csv
import datetime

gn = GoogleNews(lang = 'en', country='US')

def get_news(topic):

    file = '../dataset/news_links/tech_theverge.csv'
    editor = 'The Verge'
    
    search = gn.search(query=topic, from_=datetime.date(2022,1,1).strftime(f'%Y-%m-%d'), to_=datetime.date(2022,5,1).strftime(f'%Y-%m-%d'))
    news_item = search['entries']
    with open(file, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for index, item in enumerate(news_item):
            if item['source']['title'] == editor:
                writer.writerow([index + 153, item['title'], item['published'], item['source']['title'], item['source']['href'], item['link']])
    return

# News site name
site = 'The Verge'
# News theme
get_news(f'technology {site}')