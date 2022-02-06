import pandas
import collections


def fetch_wines_catalog():
    excel_wines_catalog = pandas.read_excel('wine.xlsx',
                                      na_values=['N/A', 'NA'],
                                      keep_default_na=False,
                                      usecols=['Категория', 'Название',
                                               'Сорт', 'Цена',
                                               'Картинка', 'Акция']
                                      )
    wines = excel_wines_catalog.to_dict(orient='records')
    wines_catalog = collections.defaultdict(list)
    for wine in wines:
        category = wine['Категория']
        wines_catalog[category].append(wine)
    sorted_wines_catalog = collections.OrderedDict(sorted(wines_catalog.items()))
    return sorted_wines_catalog
