from aiogram import types
from aiogram.utils import markdown

from sqlalchemy import Update, TIMESTAMP
from sqlalchemy import func, cast
from sqlalchemy.sql.expression import select, update

from loguru import logger
from datetime import datetime, timedelta
from ._base import BaseSending
from ..models import async_session, User

# For future

__all__ = ["Sending2Hours", "Sending24Hours"]


class Sending2Hours(BaseSending):
    is_active = False
    text = f''
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("", url=''))

    to_log: str = '2h_sending'

    def requirements(self):
        return ((User.registration_date + timedelta(hours=2)) < datetime.now(),
                User.got_2h_autosending.is_(None), User.stage != 'stage_4', User.status == 'alive')

    def _update_query_on_success(self, user: int) -> Update:
        return update(User).where(User.id == user).values(got_2h_autosending=func.now())

    async def start(self):
        try:
            if self.is_active and self._verify():
                return await super().start()
        except ValueError as ex:
            logger.info(f'Sending2Hours {ex.args}')


class Sending24Hours(BaseSending):
    is_active = False
    text = f''
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("", url=''))
    to_log: str = '24h_sending'

    def requirements(self):
        return ((User.got_2h_autosending + timedelta(hours=22)) < datetime.now(),
                User.got_24h_autosending.is_(None), User.stage != 'stage_4', User.status == 'alive')

    def _update_query_on_success(self, user: int) -> Update:
        return update(User).where(User.id == user).values(got_24h_autosending=func.now())

    async def start(self):
        try:
            if self.is_active and self._verify():
                await super().start()
        except ValueError as ex:
            logger.info(f'Sending24Hours {ex.args}')
