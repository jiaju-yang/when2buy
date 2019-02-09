# -*- coding: utf-8 -*-
import scrapy
import collections


class StorageConfig(collections.namedtuple('StorageConfig', 'target, keys')):
    def __new__(cls, target: str, keys: tuple = ()):
        """

        @target: mongo collection name 或 sql table name
        @keys: mongo filter关键字列表，如：('id',)
        """
        return super().__new__(cls, target, keys)


class BaseItem(scrapy.Item):
    data = scrapy.Field()


class FlightItem(BaseItem):
    class Meta:
        """航班

        """
        sql = StorageConfig(target='flights')
