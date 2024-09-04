import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = list()
        years_set = set()
        # i = 0
        for row in reader:
            iterable =  zip(header, row)
            data_dict = {key: value for key, value in iterable}
            years_set.add(int(data_dict['Year']))
            data.append(data_dict)
            # if i == 5:
                # break    # Cambiar despues para iterar sobre todos
            # i += 1
        return data, years_set
    


if __name__ == '__main__':
    data, years = read_csv('./app/tortilla_prices.csv')
    print(years)
