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

    def create(self, stat: tuple[Row[datetime, int]]) -> Path:
        self.path.unlink(missing_ok=True)

        wb = Workbook()
        ws: Worksheet = wb.active
        for row in stat:
            row = [row.date, row.count]
            ws.append(row)
        wb.save(self.path)
        return self.path


class StagesExcelStat(_BaseExcelStat):
    path = DATA_DIR / 'stages.xlsx'

    def create(self, stat):
        ...
