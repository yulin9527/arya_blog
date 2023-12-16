from nicegui import ui

from app.view.page.admin import admin_page
from app.view.page.home import main_page
from app.view.page.login import login_page

# 主页
ui.page('/')(main_page)


# 登录注册页
ui.page('/login')(login_page)

ui.page('/admin')(admin_page)