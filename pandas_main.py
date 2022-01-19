import pandas
from pprint import pprint
from collections import defaultdict


def fetch_wines():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
                                      usecols=['Название', 'Сорт', 'Цена',
                                               'Картинка'])
    wines = excel_data_df.to_dict(orient='record')
    return wines


def fetch_wines_new():
    excel_data_df = pandas.read_excel('wine_new.xlsx', na_values=['N/A', 'NA'],
                                      keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records') #список словарей
    catalog_wines = defaultdict(list)
    for wine in wines:
        category = wine['Категория']
        catalog_wines[category].append(wine)
    pprint(catalog_wines)
    return catalog_wines


fetch_wines_new()
