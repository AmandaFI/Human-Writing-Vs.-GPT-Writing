import requests
from bs4 import BeautifulSoup
import csv

path = r'../scraped_news_links/tech_theverge.csv'
with open(path, 'r', encoding="utf-8") as info_file:

    csv_reader = csv.reader(info_file, delimiter=',')
    editor = 'The Verge'

    for row in csv_reader:

        if len(row) > 0:
            url = row[5]
            r1 = requests.get(url)
            content = r1.content

            soup1 = BeautifulSoup(content, 'html.parser')

            div_content = soup1.find_all('article')
            if div_content:
                news_text = div_content[0].find_all(['p', 'h1', 'h2', 'li'])
                
                full_text = ''
                for tag in news_text[2:]:
                    if full_text != '' and full_text[-1] != ' ':
                        full_text += ' '
                
                    text = tag.get_text()
                    if 'Featured Videos From The Verge' in text or 'Verge Deals' in text:
                        break
                    elif 'Share this story' in text:
                        pass
                    elif 'inline selection:bg-franklin-20' in str(tag) or 'duet--article--article-byline' in str(tag) or 'duet--article--date-and-comments' in str(tag) or 'bg-repeating-lines-dark' in str(tag) or 'text-gray-4a' in str(tag) or 'font-polysans' in str(tag):
                       pass
                    elif '<h1>' in str(tag):
                        full_text += '. '
                    else:
                        full_text += text

                with open(f'TheVerge/{row[0]}_TheVerge.txt', 'w', encoding="utf-8") as file:
                    file.write(full_text)

            