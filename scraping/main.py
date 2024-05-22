
from bs4 import BeautifulSoup
import pandas as pd
with open("qoutes.html","r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, "html.parser")



quotes = soup.select('div.quoteText')


data = []
for quote in quotes:
    quote_text = quote.contents[0].strip().replace('“', '').replace('”', '')
    author = quote.find('span', class_='authorOrTitle').string.strip()
    data.append({'quote': quote_text, 'author': author})


df = pd.DataFrame(data)


grouped_df = df.groupby('author')['quote'].apply(lambda x: ' | '.join(x)).reset_index()

grouped_df.to_csv('quotes_grouped.csv', index=False)

