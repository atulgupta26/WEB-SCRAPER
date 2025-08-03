import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://example.com'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract all article titles and links
data = []
for article in soup.find_all('article'):
    title = article.find('h2').get_text(strip=True)
    link = article.find('a')['href']
    data.append({'title': title, 'link': link})

# Save to CSV
with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)