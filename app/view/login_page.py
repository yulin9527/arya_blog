from nicegui import ui

from app.core.servers import Server


@ui.page('/')
async def page_login():
    ui.input(label='账号', placeholder='请输入账号',
             on_change=lambda e: result.set_text('你的账号是: ' + e.value),
             validation={'Input too long': lambda value: len(value) < 20})
    ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'), )
    result = ui.label()

    with ui.card() as a:
        ui.label('card content')
        ui.button('添加标签', on_click=lambda: a.clear())
        ui.timer(10.0, lambda: ui.label('tick'), once=True)
        with ui.card_section():
            ui.label('123')
            ui.button('添加标签', on_click=lambda: ui.label('arya'))
    print(result)

    # 基本使用
    with ui.card():
        ui.label('这是一个card')

    # 删除阴影 设置边框宽度
    with ui.card().classes('no-shadow border-[1px]'):
        ui.label('删除了阴影')

    columns = [{'name': 'age', 'label': 'Age', 'field': 'age'}]
    rows = [{'age': '16'}, {'age': '18'}, {'age': '21'}]

    # 嵌套使用
    with ui.row():
        with ui.card():
            ui.table(columns, rows).props('flat bordered')
        # 删除 card 的边距
        with ui.card().tight():
            ui.table(columns, rows).props('flat bordered')
        with ui.card():
            with ui.row():
                ui.table(columns, rows).props('flat bordered')

    with ui.column():
        ui.label('label 1')
        ui.label('label 2')
        ui.label('label 3')

    with ui.element('div').classes('columns-3 w-full gap-2'):
        for i, height in enumerate([50, 50, 50, 150, 100, 50]):
            tailwind = f'mb-2 p-2 h-[{height}px] bg-blue-100 break-inside-avoid'
            with ui.card().classes(tailwind):
                ui.label(f'Card #{i + 1}')

    container = ui.row()

    def add_face():
        with container:
            ui.icon('face')

    add_face()

    ui.button('Add', on_click=add_face)
    ui.button('Remove', on_click=lambda: container.remove(0) if list(container) else None)
    ui.button('Clear', on_click=container.clear)

    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('One')
        two = ui.tab('Two')
    with ui.tab_panels(tabs, value=two).classes('w-full'):
        with ui.tab_panel(one):
            ui.label('First tab')
        with ui.tab_panel(two):
            ui.label('Second tab')
    with ui.stepper().props('vertical').classes('w-full') as stepper:
        with ui.step('Preheat'):
            ui.label('Preheat the oven to 350 degrees')
            with ui.stepper_navigation():
                ui.button('Next', on_click=stepper.next)
        with ui.step('Ingredients'):
            ui.label('Mix the ingredients')
            with ui.stepper_navigation():
                ui.button('Next', on_click=stepper.next)
                ui.button('Back', on_click=stepper.previous).props('flat')
        with ui.step('Bake'):
            ui.label('Bake for 20 minutes')
            with ui.stepper_navigation():
                ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
                ui.button('Back', on_click=stepper.previous).props('flat')


# @ui.page('/arya')
# async def login_demo():
#     ui.input(label='Text', placeholder='start typing',
#              on_change=lambda e: result.set_text('you typed: ' + e.value),
#              validation={'Input too long': lambda value: len(value) < 20})
#     ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'), )
#     result = ui.label()


@ui.page('/other_page')
def other_page():
    ui.label('Welcome to the other side')
    response = Server.client.get('/9527')
    print(response.json())
    print('---->>>>>')
    ui.link('Back to main page', '/dark_page')


@ui.page('/dark_page', dark=True)
def dark_page():
    ui.label('Welcome to the dark side')
    ui.link('Back to main page', '/other_page')
