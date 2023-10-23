from sqlalchemy.orm import declarative_base, mapped_column, Mapped

from sqlalchemy import (
    BIGINT,
    String,
    TIMESTAMP,
    func
)

from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    registration_date: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    stage: Mapped[str | None] = mapped_column(String(64))

    got_2h_autosending: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    got_24h_autosending: Mapped[datetime | None] = mapped_column(TIMESTAMP)
