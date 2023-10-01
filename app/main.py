import pandas as pd
from dataclasses import dataclass, asdict
import requests
from rich import print
from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright


@dataclass
class movies_list:
    id: int
    film_name: str
    id_imdb: str
    url: str


@dataclass
class review_data:
    id: int
    name: str
    text: str
    date: str
    rating: str


def get_id_imdb(film_name: str, id: int) -> movies_list:
    json_data = requests.get(
        f"https://v3.sg.media-imdb.com/suggestion/x/{film_name}.json"
    )
    id_imdb = json_data.json()["d"][0]["id"]
    url_review = f"https://www.imdb.com/title/{id_imdb}/reviews/"
    item = movies_list(id=id, film_name=film_name, id_imdb=id_imdb, url=url_review)
    return item


def read_xlsx() -> list:
    xlsx_data = "movies_list.xlsx"
    df = pd.read_excel(xlsx_data, sheet_name="list", index_col=0)
    return df["movie_title"].tolist()


def movies():
    movies = []
    id = 1
    for item in read_xlsx():
        movies.append(asdict(get_id_imdb(item, id)))
        id += 1
        # break
        if id == 5:
            break
    return movies


def get_html(page, id):
    url = f"https://www.imdb.com/title/{id}/reviews?sort=submissionDate&dir=desc&ratingFilter=0"
    print(url)
    page.goto(url)
    html = HTMLParser(page.content())
    return html


def get_reviews(page):
    review_d = []
    id = 1
    for item in movies():
        html = get_html(page, item["id_imdb"])

        for review in html.css("div.lister-item"):
            try:
                rating = (
                    review.css_first("div.ipl-ratings-bar")
                    .text(strip=True)
                    .split("/")[0]
                )
            except:
                rating = ""

            item = review_data(
                id=id,
                name=review.css_first("span.display-name-link").text(strip=True),
                text=review.css_first("div.text").text(strip=True),
                date=review.css_first("span.review-date").text(strip=True),
                rating=rating,
            )
            review_d.append(asdict(item))

        id += 1
    return review_d


def run():
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    page = browser.new_page()
    reviews = get_reviews(page)
    print(reviews)
    browser.close()
    pw.stop()


def main():
    run()


if __name__ == "__main__":
    main()
