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
    catalog_wines = collections.defaultdict(list)
    for wine in wines:
        category = wine['Категория']
        catalog_wines[category].append(wine)
    catalog_wines_sorted = collections.OrderedDict(sorted(catalog_wines.items()))
    return catalog_wines_sorted
