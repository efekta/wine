from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas_main import fetch_wines_catalog
import datetime
import argparse


WINERY_YEAR_BIRTH = 1920
WINERY_AGE = str(datetime.date.today().year - WINERY_YEAR_BIRTH)


def main():
    parser = argparse.ArgumentParser(description='Описание программы')
    parser.add_argument('file_path', type=str, help='Путь к файлу',
                        default='wine.xlsx')
    args = parser.parse_args()
    file_path = args.file_path

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    winery_catalog = fetch_wines_catalog(file_path)
    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=WINERY_AGE,
        winery_catalog=winery_catalog,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
