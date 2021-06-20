from src.config.loader import dp
from .is_admin import AdminFilter
if __name__ == "filters":
    dp.bind_filter(is_admin)
