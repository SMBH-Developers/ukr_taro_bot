from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from pathlib import Path
from datetime import datetime
from sqlalchemy import Row

from abc import ABC, abstractmethod
from ...constants import DATA_DIR


class _BaseExcelStat(ABC):
    path: Path = ...

    @abstractmethod
    def create(self, stat):
        raise NotImplementedError


class UsersExcelStat(_BaseExcelStat):
    path = DATA_DIR / 'users.xlsx'

    @staticmethod
    def _prepare_columns(ws: Worksheet):
        ws.column_dimensions['A'].width = 25
        ws.column_dimensions['B'].width = 15

    def create(self, stat: tuple[Row[datetime, int]]) -> Path:
        self.path.unlink(missing_ok=True)

        wb = Workbook()
        ws: Worksheet = wb.active
        self._prepare_columns(ws)
        for row in stat:
            row = [row.date, row.count]
            ws.append(row)
        wb.save(self.path)
        return self.path


class StagesExcelStat(_BaseExcelStat):
    path = DATA_DIR / 'stages.xlsx'

    @staticmethod
    def _prepare_columns(ws: Worksheet):
        ws.column_dimensions['A'].width = 25
        for column in 'BCDEFGH':
            ws.column_dimensions[column].width = 15

    def create(self, stat: tuple[Row[datetime, int, int, int, int, int, int]]):
        self.path.unlink(missing_ok=True)

        wb = Workbook()
        ws: Worksheet = wb.active
        self._prepare_columns(ws)

        row_titles = ['Дата', '', 'Всего', 'None', 'stage_1', 'stage_2', 'stage_3', 'stage_4']
        ws.append(row_titles)
        for row in stat:
            row = [row.date, '', row.all_stages, row.stage_null, row.stage_1, row.stage_2, row.stage_3, row.stage_4]
            ws.append(row)
        wb.save(self.path)
        return self.path
