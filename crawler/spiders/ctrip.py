import json
from datetime import datetime, timedelta

import pytz

import scrapy

import static_data
import utils
from items import FlightItem
from parsers.ctrip import parse_flights


class CtripSpider(scrapy.Spider):
    name = "ctrip"

    def start_requests(self):
        flights = [
            ('ctu', 'hgh'),
            ('sha', 'bjs'),
        ]
        now = utils.now()
        for flight in flights:
            for days in range(1, 61):
                depart_at = now + timedelta(days=days)
                yield self.gen_flight_req(flight[0], flight[1], depart_at)
                yield self.gen_flight_req(flight[1], flight[0], depart_at)

    def gen_flight_req(self, departure_city_code, arrival_city_code, depart_at: datetime) -> scrapy.Request:
        url = "https://flights.ctrip.com/itinerary/api/12808/products"
        depart_at_date = depart_at.strftime('%Y-%m-%d')
        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'referer': f'https://flights.ctrip.com/itinerary/oneway/{departure_city_code}-{arrival_city_code}?date={depart_at_date}',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,ja;q=0.5',
            'cache-control': 'no-cache,no-cache',
            'origin': 'https://flights.ctrip.com',
            'pragma': 'no-cache'
        }
        payload = {
            'flightWay': 'Oneway',
            'classType': 'ALL',
            'hasChild': False,
            'hasBaby': False,
            'searchIndex': 1,
            'airportParams': [{
                'dcity': departure_city_code,
                'acity': arrival_city_code,
                'dcityname': static_data.cities_code[departure_city_code],
                'acityname': static_data.cities_code[arrival_city_code],
                'date': depart_at_date,
            }]
        }
        return scrapy.Request(url=url, method='POST', headers=headers, body=json.dumps(payload),
                              callback=self.parse)

    def parse(self, resp: scrapy.http.Response):
        data = json.loads(resp.text)
        flights = parse_flights(data)
        for flight in flights:
            flight['source'] = 'c'
            flight['search_at'] = utils.now()
            yield FlightItem(data=flight)
