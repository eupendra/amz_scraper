import sqlite3

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


class AmazonPipeline:
    def __init__(self):
        self.cur = None
        self.con = None
        self.settings = get_project_settings()
        self.db_file = self.settings.get('SQLITE_FILE', 'db/amazon.db')
        self.connect_db()
        self.create_table()

    def process_item(self, item, spider):
        if 'in stock' in item.get('product_availability').lower():
            if not (item.get('current_price') or item.get('deal_price') or item.get('old_price')):
                raise DropItem("Price Not Found")
        self.update_db(item)
        return item

    def connect_db(self):
        self.con = sqlite3.connect(self.db_file)
        self.cur = self.con.cursor()

    def create_table(self):
        sql = """
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY NOT NULL,
                    asin text,
                    product_name text,
                    old_price NUMERIC,
                    current_price NUMERIC,
                    deal_price NUMERIC,
                    category text
                )
                """
        self.cur.execute(sql)

    def update_db(self, item):
        data: tuple = (item.get('asin'),
                       item.get('product_name'),
                       item.get('old_price'),
                       item.get('current_price'),
                       item.get('deal_price'),
                       item.get('category'))
        sql: str = "INSERT INTO products(asin, product_name, old_price, current_price, deal_price, category) \n" \
                   "VALUES (?, ?, ?, ?, ?, ?)"

        self.cur.execute(sql, data)
        self.con.commit()
