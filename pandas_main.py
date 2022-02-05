import pandas
from pprint import pprint
from collections import defaultdict
import collections


def fetch_wines():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
                                      usecols=['Категория', 'Название',
                                               'Сорт', 'Цена',
                                               'Картинка', 'Акция'])
    wines = excel_data_df.to_dict(orient='record')
    return wines



def fetch_wines_catalog():
    excel_data_df = pandas.read_excel('wine.xlsx', na_values=['N/A',
                                                                    'NA'],
                                      keep_default_na=False,
                                      usecols=['Категория', 'Название',
                                               'Сорт', 'Цена',
                                               'Картинка', 'Акция']
                                      )
    wines = excel_data_df.to_dict(orient='records')
    # catalog_wines = defaultdict(list)
    catalog_wines = collections.defaultdict(list)
    for wine in wines:

        category = wine['Категория']
        catalog_wines[category].append(wine)

    return catalog_wines

