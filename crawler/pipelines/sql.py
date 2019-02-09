from scrapy import Spider

from items import BaseItem
from storage.sql import repos


class SqlPipe:
    def process_item(self, item: BaseItem, spider: Spider):
        has_sql_config = (hasattr(item, 'Meta') and hasattr(item.Meta, 'sql'))
        if not has_sql_config:
            return item

        sql_config = item.Meta.sql
        table_name = sql_config.target
        repo_name = f'{table_name}_repo'
        data = dict(item['data'])
        repo = getattr(repos, repo_name)
        repo.save(data)

        return item
