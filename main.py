from bs4 import BeautifulSoup
import json
import requests

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.findAll('div', class_="quote")
data = []

for quote in quotes:
    result = {}

    result['text'] = quote.find('span', class_="text").text
    result['author'] = quote.find('small', class_="author").text
    result['author-link'] = quote.find('a').get('href')

    tags = quote.find('div', class_="tags").findAll('a', class_='tag')
    tags_text = []
    for tag in tags:
        text = tag.text
        tags_text.append(text)
    result['tags'] = tags_text
    data.append(result)

print(data)
