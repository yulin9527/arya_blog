from nicegui import ui

from app.view.element.article import editor_car, top_article


async def main_page():
    top_article()
    editor_car()

    ui.markdown(
        """可以使用循环来计算1到1000的和，示例代码如下：\n\n```python\ntotal = 0\n\nfor i in range(1, 1001):\n    total += i\n\nprint(total)\n```\n\n在这个示例中，我们使用了一个循环来遍历1到1000的数，并对它们进行累加，最后输出总和。""")

    def set_background(color: str) -> None:
        ui.query('body').style(f'background-color: {color}')  # 这句是关键，设置body的style

    ui.image('/static/head_img/arya.jpg').classes('w-16')
    ui.button('Blue', on_click=lambda: set_background('#ddeeff'))  # 点击后，页面背景颜色变为蓝色
    ui.button('Orange', on_click=lambda: set_background('#ffeedd'))  # 点击后，页面背景颜色变为橙色
    # ui.label('CONTENT')
    [ui.label(f'Line {i}') for i in range(100)]
    with ui.header(elevated=True).classes('items-center justify-between'):  # .style('background-color: #3874c8')
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

    with ui.left_drawer(top_corner=False, bottom_corner=False) as left_drawer:  # .style('background-color: #d7e3f4')
        personal_info()
        left_path_home()
        essay_class(essay_list)
        ui.separator()
        ui.separator()
        with ui.card():
            with ui.row():
                ui.button('主页')
                ui.button('评论')
                ui.button('github')
                ui.button('登录')
    with ui.right_drawer(fixed=False, top_corner=True).props(
            'bordered') as right_drawer:  # .style('background-color: #ebf1fa')
        ui.label('RIGHT DRAWER')
    with ui.footer():  # .style('background-color: #3874c8')
        ui.label('FOOTER')


def personal_info():
    # 头像小组件
    with ui.card().classes('w-full'):
        with ui.row():
            # ui.avatar('img:/static/head_img/arya.jpg', square=True, rounded=False, size='xl').classes('no-margin')
            ui.image('/static/head_img/arya.jpg').classes('w-16').style('border-radius:10px')
            # ui.image('/static/head_img/arya.jpg').classes('w-16').style('border-radius:10px')
            with ui.column():
                ui.label('羽林').style(
                    'font-weight:bold; font-size:18px;width:100%; text-align: center;')
                ui.label('What are you prepared to do?').style('font-size:12px;font-style:italic')


essay_list = ['分类1', '分类 2', '分类 3']


def essay_class(essay_list):
    with ui.card().tight().classes('w-full'):
        with ui.expansion('分类!', icon='work'):
            for essay in essay_list:
                ui.label(essay)
        ui.separator()
        with ui.expansion('页面', icon='work'):
            pass


def left_path_home():
    with ui.card().tight().classes('w-full'):
        ui.label('首页')
        ui.label('相册')
        ui.label('日记')
        ui.label('关于')


def left_title():
    with ui.card().tight().classes('w-full'):
        for i in []:
            pass
