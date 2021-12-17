import csv

reviews_base_url = 'https://www.amazon.com/product-reviews/{}'
products_base_url = 'https://www.amazon.in/dp/{}'


def get_products() -> list:
    product = []
    with open('amazon/config/asin.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # header
            if row[0]:
                product.append({
                                     'asin': row[0],
                                     'threshold': row[1]
                                 })
        return product


# print(get_products())
products = get_products()
