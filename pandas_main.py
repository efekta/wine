import pandas
from pprint import pprint


def fetch_wines():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
                                      usecols=['Название', 'Сорт', 'Цена',
                                               'Картинка'])
    wines = excel_data_df.to_dict(orient='record')

    return wines

def fetch_wines_new():
    wines_catalog = {}
    wine_catalog = []
    excel_data_df = pandas.read_excel('wine_new.xlsx')
    wines = excel_data_df.to_dict(orient='records') #список словарей
    # print(type(wines))
    print(wines)
    for wine in wines:
        # print(wine)
        category = wine['Категория']
        print(category)
        name = wine['Название']
        print(name)
        print(wine.values())
        wine_list = wine
        wines_catalog[category] = wine_list
        print(wines_catalog)
        break
    #     wine_catalog.append(wine)
    # print(wine_catalog)
        # wines_catalog[category] = wine
    # print(wines_catalog)
        # break
        # break
        # for key, item in wine.items():
        #     print(key)
        #     print(item)




fetch_wines_new()