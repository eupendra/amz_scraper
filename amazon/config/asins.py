import csv
reviews_base_url = 'https://www.amazon.com/product-reviews/{}'
products_base_url = 'https://www.amazon.com/dp/{}'


def get_asin_list() -> list:
    asin_list = []
    with open('amazon/config/asin.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0:
                continue #header
            if row[0]:
                asin_list.append(row[0])
        return asin_list


print(get_asin_list())
asin_list = get_asin_list()

# asin_list = [
#     'B08FXPDLLX',
#     'B06VWZWV6L',
#     'B08B51GQGQ',
#     'B01IR0VS3C',
#     'B079C5MJ2N',
#     'B0754QPJFH',
#     'B07D4CQC61',
#     'B00MHRGFJO',
#     'B07PWKJYFK',
#     'B01CRIM9X8',
#     'B08BP8PGMM',
#     'B07B1JQQD2',
#     'B08CSK2YNJ',
#     'B07JCS146H',
#     'B01NH0QL3A',
#     'B07VJ585NY',
#     'B07V2LRWSP',
#     'B08F518XZ8',
#     'B08BRVDST5',
#     'B074PHSKYX',
#     'B07RJNJCMF',
#     'B08DNKZLGM',
#     'B084D28G51',
#     'B00CERXZU4',
#     'B088VWRGV9',
#     'B088D5T7GR',
#     'B07TXKSNBB',
#     'B07BB7ZVNL',
#     'B08MX7Z3R3',
#     'B07RKL7L7W'
# ]
