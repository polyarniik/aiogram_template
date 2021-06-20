from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def check(self, *args) -> bool:
        # There you must filter users with our logic and return bool parameter
        return False
