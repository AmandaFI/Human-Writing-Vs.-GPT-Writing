import requests
from bs4 import BeautifulSoup
import csv

with open(r'../scraped_news_links/tech_bbc.csv', 'r') as info_file:

    csv_reader = csv.reader(info_file, delimiter=',')
    editor = 'BBC'

    for row in csv_reader:

        if len(row) > 0:
            url = row[5]
            r1 = requests.get(url)
            content = r1.content

            soup1 = BeautifulSoup(content, 'html.parser')

            div_content = soup1.find_all('article')
            if div_content:
                news_text = div_content[0].find_all(['p', 'h1', 'h2'])
                
                full_text = ''
                for tag in news_text[1:]: 
                    text = tag.get_text()
                    if 'Related Topics' in text:
                        break
                    elif 'Allow Twitter content' in text:
                        print(f'{row[0]}_{editor}')
                        break
                    elif 'This article contains content provided by Twitter. We ask for your permission before anything is loaded,' in text:
                        print(f'{row[0]}_{editor}')
                        break
                    elif '<h2>' in str(tag):
                        if 'StyledHeading' in str(tag):
                            full_text += text
                    elif '<h1>' in str(tag):
                        full_text += '. '
                    else:
                        full_text += text
                        full_text += ' '

                with open(f'{editor}/{row[0]}_{editor}.txt', 'w', encoding="utf-8") as file:
                    file.write(full_text)

            