# IMDb_rewievs
Scraping IMDb reviews

## Task
I have a sample of around 4,000 movies, and I need to extract the first 500 IMDb reviews (the first 500 in terms of review date), along with related information for each movie.
I attach an excel file.  In the first sheet there's the list of movies and related ID.
In the second sheet I noted all the info I need, and how the dataset should be structured.

## links
https://v3.sg.media-imdb.com/suggestion/x/Igby%20Goes%20Down%20(2002).json curl for requests
"id": "tt0280760",
"y": 2002
https://www.imdb.com/title/tt0280760 - search link
https://www.imdb.com/title/tt0280760/reviews/   - reviews
https://www.imdb.com/title/tt0280760/reviews/_ajax
https://www.imdb.com/title/tt0378947/reviews/_ajax?ref_=undefined&paginationKey=g4w6ddbmqyzdo6ic4oxwjmrsr3s4qbry3iptr7peadd7qwt5pjt6udc2oy3ftnzmb4d7zl5ccstrlirmnnrvu342tmrqg

## libraries

requests, selectolax, pandas

## tags

span.display-name-link user review

