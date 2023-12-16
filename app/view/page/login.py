from nicegui import ui
from nicegui import app as nice_app

from app import client


async def on_log(account, password, button):
    user = await client.post('/token', data={'username': account, "password": password})
    if user.status_code == 200:
        data = user.json()
        token = f"{data['token_type']} {data['access_token']}"
        nice_app.storage.user['token'] = token
        nice_app.storage.user['id'] = data['user_id']
        ui.open('/')
    else:
        button.text = '重新登录'


def login_page():
    ui.query('body').style(f'background:url(/static/conf_file/e03cae36ca9e41bc82ed29c825b08646.jpg)'
                           f' no-repeat center top; background-size:cover; background-attachment:fixed;')

    with ui.card().tight().classes('h-min w-1/2').style(
            'position: absolute;margin:auto;top:0;right:0;bottom:0;left:0;opacity: 0.7;'):
        with ui.grid():
            label1 = ui.label('欢迎访问').tailwind('text-center text-2xl text-dark my-2')
            account = ui.input('账号').props('outlined').style(
                'padding-left:2.5rem;padding-right:2.5rem;')
            password = ui.input('密码', password=True).props('outlined').style(
                'padding-left:2.5rem;padding-right:2.5rem;')
            with ui.row().style('justify-content: space-around'):
                link1 = ui.link('忘记密码')
                link2 = ui.link('注册账号')

            button = ui.button('登录', on_click=lambda: on_log(account.value, password.value, button)).style(
                'padding-left:2.5rem;padding-right:2.5rem;')
