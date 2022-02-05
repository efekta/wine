from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from age_winery_calc import age_winery_calc
from pandas_main import fetch_wines_catalog


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

age_winery = str(age_winery_calc())
catalog_wines = fetch_wines_catalog()
template = env.get_template('template.html')


rendered_page = template.render(
    age_winery=age_winery,
    catalog_wines=catalog_wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
