import requests
from bs4 import BeautifulSoup
import csv

path = r'../scraped_news_links/tech_techCrunch.csv'
with open(path, 'r') as info_file:

    csv_reader = csv.reader(info_file, delimiter=',')
    editor = 'TechCrunch'

    for row in csv_reader:

        if len(row) > 0:
            url = row[5]
            r1 = requests.get(url)
            content = r1.content

            soup1 = BeautifulSoup(content, 'html.parser')

            div_content = soup1.find_all('div', class_='article-content')

            news_text = div_content[0].find_all(['p', 'h2'])
            
            full_text = ''
            for tag in news_text[:-2]:
                if full_text != '' and full_text[-1] != ' ':
                    full_text += ' '

                if 'wp-embed-heading' in str(tag) or 'wp-caption-text' in str(tag) or '<p></p>' in str(tag) or '<h2></h2>' in str(tag):
                    pass
                else:
                    full_text += tag.get_text()
                if '<h2>' in str(tag):
                    full_text += '.'
               

            text = news_text[-2].get_text()
            if '<p></p>' not in str(news_text[-2]) and '<h2></h2>' not in str(news_text[-2]) and ('.' in news_text[-2].get_text()[-3:] or '!' in news_text[-2].get_text()[-3:] or '?' in news_text[-2].get_text()[-3:]):
                full_text += text

            text = news_text[-1].get_text()
            if '<p></p>' not in str(news_text[-1]) and '<h2></h2>' not in str(news_text[-1]) and ('.' in news_text[-1].get_text()[-3:] or '!' in news_text[-1].get_text()[-3:] or '?' in news_text[-1].get_text()[-3:]):
                full_text += text


            with open(f'{editor}/{row[0]}_{editor}.txt', 'w', encoding="utf-8") as file:
                file.write(full_text)
            