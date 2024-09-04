import pkg

def run():
    data, years = pkg.read_csv.read_csv('./app/tortilla_prices.csv')
    years = sorted(years)
    min_year = min(years)
    max_year = max(years)
    while True:
        try:
            print(f'Aviable years => {years}')
            year_start = input('Type start range year => ')
            year_end = input('Type end range year => ')
            if int(year_start) < min_year  or int(year_end) > max_year or int(year_end) < min_year  or int(year_end) <= int(year_start) :
                raise ValueError("El año de inicio o el año de fin están fuera del rango permitido.")

            found_years, prices = pkg.utils.get_prices_per_kilogram_per_year(data, year_start, year_end)
            pkg.charts.generate_bar_chart(found_years, prices)
        except ValueError as error:
            print(error)
if __name__ == '__main__':
    run()
    _