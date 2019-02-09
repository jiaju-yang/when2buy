from sqlalchemy import Table, select
from sqlalchemy.dialects.postgresql import insert

from .db import engine
from .tables import flights_table


class Repo:
    def __init__(self, table: Table):
        self.table = table

    def save(self, data: dict):
        data_with_exist_fields = self._remove_non_exist_columns(data)
        data_with_no_none_fields = self._trim_nothing_fields(data_with_exist_fields)
        with engine.connect() as conn:
            stmt = insert(self.table).values(
                **data_with_no_none_fields)
            conn.execute(stmt)

    def _trim_nothing_fields(self, a_dict):
        return {
            key: value
            for key, value in a_dict.items()
            if value is not None
        }

    def _remove_non_exist_columns(self, a_dict: dict):
        exist_columns = {c.name for c in self.table.columns}
        return {key: value
                for key, value in a_dict.items()
                if key in exist_columns}


flights_repo = Repo(flights_table)
