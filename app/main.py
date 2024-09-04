import pkg
import pkg.charts

def run():
    data = pkg.read_csv.read_csv('./app/tortilla_prices.csv')
    # year = input('Type year => ')
    # prices = pkg.utils.get_prices_per_kilogram_by_year(data, year)

    year_start = input('Type start range year => ')
    year_end = input('Type end range year => ')
    years, prices = pkg.utils.get_prices_per_kilogram_per_year(data, year_start, year_end)
    pkg.charts.generate_bar_chart(years, prices)

if __name__ == '__main__':
    run()
    