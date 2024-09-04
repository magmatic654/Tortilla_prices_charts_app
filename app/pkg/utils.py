def get_prices_per_kilogram_by_year(data, year):
        try:
            prices_per_kilogram_list = [float(item['Price per kilogram']) for item in data if item['Price per kilogram'] != '' and item['Year'] == year]
            prices_per_kilogram_list_len = len(prices_per_kilogram_list)
            return year, round(sum(prices_per_kilogram_list) / prices_per_kilogram_list_len, 2)
        except ZeroDivisionError:
             print(f'No se encontraron datos sobre {year}')
             return None, None

def get_prices_per_kilogram_per_year(data, start, end):
        try:
            start = int(start)
            end = int(end)
            years = [str(year) for year in range(start, end+1)]
            result_prices_list = list()
            result_years_list = list()
            for year in years:
                years_result, prices_result = get_prices_per_kilogram_by_year(data, year)
                if years_result == None:
                     continue
                
                result_prices_list.append(prices_result)
                result_years_list.append(years_result)
                
            return result_years_list, result_prices_list
        except ZeroDivisionError:
             return 'No se encontraron datos sobre ese año'


if __name__ == '__main__':
    average_prices = get_prices_per_kilogram_per_year([{'State': 'Aguascalientes', 'City': 'Aguascalientes', 'Year': '2007', 'Month': '1', 'Day': '10', 'Store type': 'Mom and Pop Store', 'Price per kilogram': '9.9'}, {'State': 'BajaÂ\xa0California', 'City': 'Mexicali', 'Year': '2007', 'Month': '1', 'Day': '10', 'Store type': 'Mom and Pop Store', 'Price per kilogram': ''}, {'State': 'BajaÂ\xa0California', 'City': 'Tijuana', 'Year': '2007', 'Month': '1', 'Day': '10', 'Store type': 'Mom and Pop Store', 'Price per kilogram': '10.0'}, {'State': 'BajaÂ\xa0CaliforniaÂ\xa0Sur', 'City': 'LaÂ\xa0Paz', 'Year': '2007', 'Month': '1', 'Day': '10', 'Store type': 'Mom and Pop Store', 'Price per kilogram': '10.0'}, {'State': 'Campeche', 'City': 'Campeche', 'Year': '2007', 'Month': '1', 'Day': '10', 'Store type': 'Mom and Pop Store', 'Price per kilogram': '10.0'}, {'State': 'Coahuila', 'City': 'PiedrasÂ\xa0Negras', 'Year': '2007', 'Month': '1', 'Day': '10', 'Store type': 'Mom and Pop Store', 'Price per kilogram': '10.0'}], 2007, 2024)

    print(average_prices)