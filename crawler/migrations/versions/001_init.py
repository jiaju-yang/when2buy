"""Init

Revision ID: 33e5db2050bf
Revises: 
Create Date: 2019-02-09 16:51:22.041758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33e5db2050bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('flight_number', sa.String(length=20), nullable=True, comment='航班号，例：CN9985'),
    sa.Column('lowest_price', sa.Integer(), nullable=True, comment='该航班最低价格'),
    sa.Column('plane_type_code', sa.String(length=20), nullable=True, comment='飞机型号代码'),
    sa.Column('airline_code', sa.String(length=20), nullable=True, comment='航空公司代码'),
    sa.Column('departure_city_code', sa.String(length=10), nullable=True, comment='出发城市代码'),
    sa.Column('departure_airport_code', sa.String(length=10), nullable=True, comment='出发机场代码'),
    sa.Column('departure_terminal_id', sa.Integer(), nullable=True, comment='出发航站楼代码'),
    sa.Column('arrival_city_code', sa.String(length=10), nullable=True, comment='到达城市代码'),
    sa.Column('arrival_airport_code', sa.String(length=10), nullable=True, comment='到达机场代码'),
    sa.Column('arrival_terminal_id', sa.Integer(), nullable=True, comment='到达航站楼代码'),
    sa.Column('depart_at', sa.DateTime(timezone=True), nullable=True, comment='计划起飞时间'),
    sa.Column('arrive_at', sa.DateTime(timezone=True), nullable=True, comment='计划降落时间'),
    sa.Column('punctual_rate', sa.Float(), nullable=True, comment='准点率'),
    sa.Column('stop_times', sa.SmallInteger(), nullable=True, comment='经停次数'),
    sa.Column('source', sa.String(length=1), nullable=True, comment='数据来源'),
    sa.Column('search_at', sa.DateTime(timezone=True), nullable=True, comment='查询时间')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flights')
    # ### end Alembic commands ###
