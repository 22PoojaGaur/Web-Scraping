import requests
import bs4
from typing import List, Tuple


def get_page_url(date: str) -> str:
    return f'https://www.boxofficemojo.com/date/{date}'


def box_office_movie_collection(date: str) -> List[Tuple]:
    page = get_page_url(date)
    print(f'debug -> url constructed {page}')
    request_on_page = requests.get(page)
    soup = bs4.BeautifulSoup(request_on_page.text, 'html.parser')

    tables = soup.select('table')
    rows = tables[0].select('tr')

    result: List[Tuple] = []
    for row in rows[1:]:
        cols = row.select('td')
        result.append((cols[2].getText(), cols[3].getText()))

    return result


if __name__ == '__main__':
    date = str(input("Enter date for a day movie collection->\n"))
    movie_collection_per_day = box_office_movie_collection(date)
    for i in movie_collection_per_day:
        print(i[0] + '|' + i[1])
        print('\n')






