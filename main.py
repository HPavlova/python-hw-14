from bs4 import BeautifulSoup
import json
import requests


def main():
    url = 'https://quotes.toscrape.com/page/{}/'
    data = []

    for page in range(1, 3):
        response = requests.get(url.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.findAll('div', class_="quote")

        for quote in quotes:
            result = {}

            result['text'] = quote.find('span', class_="text").text.replace('“', '').replace('”', '')
            result['author'] = quote.find('small', class_="author").text
            result['author-link'] = quote.find('a').get('href')

            tags = quote.find('div', class_="tags").findAll('a', class_='tag')
            tags_text = []
            for tag in tags:
                text = tag.text
                tags_text.append(text)
            result['tags'] = tags_text
            data.append(result)
    with open('quotes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
