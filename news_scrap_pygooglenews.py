from pygooglenews import GoogleNews
import csv
import datetime

gn = GoogleNews(lang = 'en', country='US')

def get_news(topic):

    file = 'tech_theverge_3.csv'
    editor = 'The Verge'
    
    # search = gn.search(query=topic, when='1m')
    # primero foi 01/01/2023 até 17/04/2023
    # segundo foi 18/04/2022 até 26/04/2023
    # terceito foi 01/01/2022 até 01/06/2022
    search = gn.search(query=topic, from_=datetime.date(2022,1,1).strftime(f'%Y-%m-%d'), to_=datetime.date(2022,5,1).strftime(f'%Y-%m-%d'))
    news_item = search['entries']
    with open(file, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for index, item in enumerate(news_item):
            if item['source']['title'] == editor:
                writer.writerow([index + 153, item['title'], item['published'], item['source']['title'], item['source']['href'], item['link']])
    return

site = 'The Verge'
get_news(f'technology {site}')










    # search = gn.topic_headlines('BUSINESS', proxies=None, scraping_bee = None)


# business = gn.topic_headlines('BUSINESS', proxies=None, scraping_bee = None)

# TODO

# verificar noticias pois algumas podem nao ser do site desejado, deletera essas
# criar scrape para cada um dos sites
# fazer o scrape de cada noticia

# escolher alguns sites/editores confiaveis e montar x noticias de cada site
# escolher temas atuais e pegar noticias depois do fim de 2021
# primeiro fazer um df/csv com as informacoes das noticias obtidas pelo pygooglenews e seus links
# depois criar folders por editor/site e dentro deles um arquivo por noticia 

# para conseguir mais de 100 artigos fazer por intervalos de tempo
# asism conseguira 100 de cada intervalo de tempo
# gn.search(search, from_=date.strftime('%Y-%m-%d'), to_=(date+delta).strftime('%Y-%m-%d'))

# keys --> dict_keys(['title', 'title_detail', 'links', 'link', 'id', 'guidislink', 'published', 'published_parsed', 'summary', 'summary_detail', 'source', 'sub_articles'])

# news --> {'title': "The Secret To Daniil Medvedev's Recent Success - ATP Tour", 'title_detail': {'type': 'text/plain', 'language': None, 'base': '', 'value': "The Secret 
# To Daniil Medvedev's Recent Success - ATP Tour"}, 'links': [{'rel': 'alternate', 'type': 'text/html', 
# 'href': 'https://news.google.com/rss/articles/CBMiR2h0dHBzOi8vd3d3LmF0cHRvdXIuY29tL2VuL25ld3MvbWVkdmVkZXYtbW9udGUtY2FybG8tMjAyMy1zdGF0cy1wcmV2aWV30gEA?oc=5'}], 
# 'link': 'https://news.google.com/rss/articles/CBMiR2h0dHBzOi8vd3d3LmF0cHRvdXIuY29tL2VuL25ld3MvbWVkdmVkZXYtbW9udGUtY2FybG8tMjAyMy1zdGF0cy1wcmV2aWV30gEA?oc=5', 
# 'id': 'CBMiR2h0dHBzOi8vd3d3LmF0cHRvdXIuY29tL2VuL25ld3MvbWVkdmVkZXYtbW9udGUtY2FybG8tMjAyMy1zdGF0cy1wcmV2aWV30gEA', 'guidislink': False, 'published': 'Tue, 11 Apr 2023 21:45:36 GMT',
#  'published_parsed': time.struct_time(tm_year=2023, tm_mon=4, tm_mday=11, tm_hour=21, tm_min=45, tm_sec=36, tm_wday=1, tm_yday=101, tm_isdst=0), 
# 'summary': '<a href="https://news.google.com/rss/articles/CBMiR2h0dHBzOi8vd3d3LmF0cHRvdXIuY29tL2VuL25ld3MvbWVkdmVkZXYtbW9udGUtY2FybG8tMjAyMy1zdGF0cy1wcmV2aWV30gEA?oc=5" 
# target="_blank">The Secret To Daniil Medvedev\'s Recent Success</a>&nbsp;&nbsp;<font color="#6f6f6f">ATP Tour</font>', 
# 'summary_detail': {'type': 'text/html', 'language': None, 'base': '', 
# 'value': '<a href="https://news.google.com/rss/articles/CBMiR2h0dHBzOi8vd3d3LmF0cHRvdXIuY29tL2VuL25ld3MvbWVkdmVkZXYtbW9udGUtY2FybG8tMjAyMy1zdGF0cy1wcmV2aWV30gEA?oc=5" 
# target="_blank">The Secret To Daniil Medvedev\'s Recent Success</a>&nbsp;&nbsp;<font color="#6f6f6f">ATP Tour</font>'}, 'source': {'href': 'https://www.atptour.com', 
# 'title': 'ATP Tour'}, 'sub_articles': []} 