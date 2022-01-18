import pandas

def fetch_wines():
    excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1',
                                      usecols=['Название', 'Сорт', 'Цена',
                                               'Картинка'])
    wines = excel_data_df.to_dict(orient='record')

    return wines