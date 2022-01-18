import pandas
from pprint import pprint


def fetch_wines():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
                                      usecols=['Название', 'Сорт', 'Цена',
                                               'Картинка'])
    wines = excel_data_df.to_dict(orient='record')

    return wines

def fetch_wines_new():
    wines_all = ('Красные вина', 'Белые вина', 'Напитки')
    wines_catalog = {}

    excel_data_df = pandas.read_excel('wine_new.xlsx')
    wines = excel_data_df.to_dict(orient='records')

    print(pprint(wines))

    for wine in wines:
        # print(wine)
        for key, item in wine.items():
            category = wine['Категория']
            # print(category)
            if category == wines_all[1]:
                print(category == wines_all[1])
                wines_catalog[category] = wine
        print(wines_catalog)
    # print(pprint(wines_all))
    # print(wines)
    # print(type(wines))
    # for wine in wines:
    #     wine_item = dict(wine)
    #     # print(wine)
    #     category = wine['Категория']
    #     print(category)
    #     print(type(category))
    #     # print(wines_all[category])
    #     wines_all[category] = wine_item
    # print(type(wines_all))
    # print(wines_all)
    # # print('\n')
    # # print('\n')
    # # print('\n')
    # # pprint(wines_all)



fetch_wines_new()