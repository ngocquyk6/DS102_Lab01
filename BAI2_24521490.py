import requests
import pandas as pd
import re

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=30)
print("Status code:", response.status_code)
html = response.text

books = re.findall(
    r'<article class="product_pod">(.*?)</article>',
    html,
    re.DOTALL
)

book_data = []

for book in books:

    title = re.search(
        r'title="([^"]+)"',
        book
    )

    price = re.search(
        r'£([\d.]+)',
        book
    )

    rating = re.search(
        r'star-rating ([A-Za-z]+)',
        book
    )

    if title and price and rating:
        book_data.append({
            "title": title.group(1),
            "price": price.group(1),
            "rating": rating.group(1)
        })

df_books = pd.DataFrame(book_data)

print(df_books.shape)

df_books.to_csv(
    "books.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df_books.head())
