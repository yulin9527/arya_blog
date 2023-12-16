from fastapi import Depends
from nicegui import ui, APIRouter

from app import fast_app
# from app.view.page.admin import admin_page
from app.view.page.home import main_page
from app.view.page.login import login_page
from nicegui import app as nice_app

from app.view.page.timeline import time_line

user_router = APIRouter(
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

user_router.page('/', )(main_page)
user_router.page('/timeline', )(time_line)
nice_app.include_router(user_router)
# 主页
# ui.page('/', )(main_page)

# 登录注册页
ui.page('/login')(login_page)

# ui.page('/admin')(admin_page)
