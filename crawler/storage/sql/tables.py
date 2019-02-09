from sqlalchemy import (Column, DateTime, Float, Integer, MetaData, String, Table, SmallInteger)

metadata = MetaData()

flights_table = Table(
    'flights', metadata,
    Column('flight_number', String(20), comment='航班号，例：CN9985'),
    Column('lowest_price', Integer, comment='该航班最低价格'),
    Column('plane_type_code', String(20), comment='飞机型号代码'),
    Column('airline_code', String(20), comment='航空公司代码'),
    Column('departure_city_code', String(10), comment='出发城市代码'),
    Column('departure_airport_code', String(10), comment='出发机场代码'),
    Column('departure_terminal_id', Integer, comment='出发航站楼代码'),
    Column('arrival_city_code', String(10), comment='到达城市代码'),
    Column('arrival_airport_code', String(10), comment='到达机场代码'),
    Column('arrival_terminal_id', Integer, comment='到达航站楼代码'),
    Column('depart_at', DateTime(timezone=True), comment='计划起飞时间'),
    Column('arrive_at', DateTime(timezone=True), comment='计划降落时间'),
    Column('punctual_rate', Float, comment='准点率'),
    Column('stop_times', SmallInteger, comment='经停次数'),
    Column('source', String(1), comment='数据来源'),
    Column('search_at', DateTime(timezone=True), comment='查询时间')
)
