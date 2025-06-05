import requests, csv, os

from bs4 import BeautifulSoup


BASE_URL = 'https://ru.wikipedia.org'
START_URL = '/wiki/Категория:Животные_по_алфавиту'
BASE_DIR = os.path.join(os.path.dirname(__file__), 'test_pages')
START_DIR = 'page1.html'


def fetch_from_web(url: str) -> str:
    response = requests.get(BASE_URL + url)
    response.raise_for_status()
    return response.text


def fetch_from_local(filename: str) -> str:
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'Файл не найден: {filepath}')
    with open(filepath, encoding='utf-8') as f:
        return f.read()


def wiki_animal_counter(url: str, result: dict, local_or_web):
    html = local_or_web(url)
    soup = BeautifulSoup(html, 'lxml')
    main_box = soup.find('div', id='mw-pages')
    category_groups = main_box.find_all('div', class_='mw-category-group')
    for category in category_groups:
        letter = category.find('h3').get_text()
        count = len(category.find_all('li'))
        if letter in result.keys():
            result[letter] += count
        else:
            result[letter] = count
    next_page = main_box.find('a', string='Следующая страница')
    if next_page is not None:
        return wiki_animal_counter(next_page.get('href'), result, local_or_web)
    return result


if __name__ == '__main__':
    result = wiki_animal_counter(START_URL, {}, fetch_from_web)
    with open('file.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for letter, count in result.items():
            writer.writerow([letter, count])
