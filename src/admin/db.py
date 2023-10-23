from sqlalchemy import func, text, desc, Row
from sqlalchemy.sql.expression import select, between

from datetime import datetime, date, timedelta

from ..models import async_session
from ..models import User


async def get_users_stat() -> tuple[int, int, int]:

    def _users_count():
        return select(func.count()).select_from(User)

    async with async_session() as session:
        all_users = (await session.execute(_users_count())).scalar_one()
        yesterday_users = (await session.execute(_users_count()
                                                 .where(User.registration_date == (date.today() - timedelta(days=1)))
                                                 )).scalar_one()
        today_users = (await session.execute(_users_count()
                                             .where(User.registration_date == date.today())
                                             )).scalar_one()

    return all_users, yesterday_users, today_users


async def get_users_excel() -> tuple[Row[datetime, int]]:
    now_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    query = (select(func.date(User.registration_date).label('date'), func.count().label('count'))
             .where(between(func.date(User.registration_date), now_date, end_date))
             .group_by(text('date')).order_by(desc(text('date'))))

    async with async_session() as session:
        stat = (await session.execute(query)).all()

    return stat


def _optimize_stages(ls_stages_stat):
    ls_stages_stat = [(stages_stat.stage, stages_stat.count) for stages_stat in ls_stages_stat]
    stages = ['stage_1', 'stage_2', 'stage_3', 'stage_4']
    db_stages = [stage_ls[0] for stage_ls in ls_stages_stat]
    for default_stage in stages:
        if default_stage not in db_stages:
            ls_stages_stat.append((default_stage, 0))
    ls_stages_stat.sort(key=lambda ls: ls if ls[0] is not None else '.')
    return ls_stages_stat


async def get_stages_stat() -> list[list[tuple], list[tuple], list[tuple]]:

    def _stages_count():
        return select(User.stage, func.count().label('count')).select_from(User).group_by(User.stage)

    async with async_session() as session:
        total_stages = (await session.execute(_stages_count())).all()
        yesterday_stages = (await session.execute(_stages_count()
                                                  .where(User.registration_date == (date.today() - timedelta(days=1)))
                                                  )).all()
        today_stages = (await session.execute(_stages_count()
                                              .where(User.registration_date == date.today())
                                              )).all()
    ls = [_optimize_stages(stages_stat) for stages_stat in (total_stages, yesterday_stages, today_stages)]
    return ls
