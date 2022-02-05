import pandas
from pprint import pprint
from collections import defaultdict
import collections


def fetch_wines():
    excel_data_df = pandas.read_excel('wine_new_2.xlsx', sheet_name='Лист1',
                                      usecols=['Категория', 'Название',
                                               'Сорт', 'Цена', 'Картинка'])
    wines = excel_data_df.to_dict(orient='record')
    return wines



def fetch_wines_catalog():
    excel_data_df = pandas.read_excel('wine_new_2.xlsx', na_values=['N/A',
                                                                    'NA'],
                                      keep_default_na=False,
                                      usecols=['Категория', 'Название',
                                               'Сорт', 'Цена', 'Картинка']
                                      )
    wines = excel_data_df.to_dict(orient='records')
    # catalog_wines = defaultdict(list)
    catalog_wines = collections.defaultdict(list)
    for wine in wines:

        category = wine['Категория']
        catalog_wines[category].append(wine)

    return catalog_wines


catalog_wines = fetch_wines_catalog()


# def fetch_wines_category(catalog_wines):
#     for key, item in catalog_wines.items():
#         print(key)
#         print(item)
#
# pprint(fetch_wines_category(catalog_wines))