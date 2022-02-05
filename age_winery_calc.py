import datetime

def age_winery_calc():
    today_data = datetime.datetime.now()
    today_year = today_data.year
    year_birth_wine = 1920
    age_winery = str(today_year - year_birth_wine)
    return age_winery
