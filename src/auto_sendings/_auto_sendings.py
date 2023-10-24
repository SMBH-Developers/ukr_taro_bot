from ._base import BaseSending

# For future

__all__ = ["Sending2Hours", "Sending24Hours"]


class Sending2Hours(BaseSending):
    text = None
    kb = None

    async def start(self):
        return
        self._verify()


class Sending24Hours(BaseSending):
    text = None
    kb = None

    async def start(self):
        return
        self._verify()
