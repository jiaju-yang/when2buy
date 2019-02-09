from sqlalchemy import create_engine

from scrapy.utils.project import get_project_settings

DB_URL = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'

settings = get_project_settings()
db_settings = settings['SQL']
engine = create_engine(DB_URL.format(**db_settings))
