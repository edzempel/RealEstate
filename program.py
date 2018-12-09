import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    data = load_file(filename)
    query_data(data)


def print_header():
    print('--------------------------------------')
    print('    REAL ESTATE DATA MINING APP')
    print('--------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # use DictReader to create more resilient code
        # using a key instead of an idex allows the columns to be added or deleted form the csv
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


# def get_price(p):
#     return p.price


def query_data(data):
    # if data was sorted by price:
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print("the most expensive house is ${:,} with {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    # least expensive house?
    low_purchase = data[0]
    print("the least expensive house is ${:,} with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    prices = []
    for pur in data:
        prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    # average price of 2 bedroom houses
    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print("The average 2-bedroom home price is ${:,}".format(int(ave_price)))


if __name__ == '__main__':
    main()
