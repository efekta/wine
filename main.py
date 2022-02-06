from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas_main import fetch_wines_catalog
import datetime


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

YEAR_BIRTH_WINERY = 1920
AGE_WINERY = str(datetime.date.today().year - YEAR_BIRTH_WINERY)
catalog_wines = fetch_wines_catalog()
template = env.get_template('template.html')


rendered_page = template.render(
    age_winery=AGE_WINERY,
    catalog_wines=catalog_wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
