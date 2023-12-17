from nicegui import ui

"""
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
"""
def top_article():
    """
    置顶轮播图
    """
    with ui.carousel(animated=True, arrows=True, navigation=False).props('infinite').classes('h-auto w-full p-0'):
        with ui.carousel_slide().classes('p-0'):
            ui.image('/static/conf_file/95a7ae21485141db897dd8ab99429709.jpg')
        with ui.carousel_slide().classes('p-0'):
            ui.image('/static/conf_file/5848e4a37f5e4fb39f4c4384a9c27523.jpg')
        with ui.carousel_slide().classes('p-0'):
            ui.image('/static/conf_file/43632a2f077b496490fdc5c6384b91fd.jpg')
        with ui.carousel_slide().classes('p-0'):
            ui.image('/static/conf_file/e03cae36ca9e41bc82ed29c825b08646.jpg')


def editor_car():
    """
    文章页面输入编辑器
    """""
    editor = ui.editor(placeholder='arya')
    ui.markdown().bind_content_from(editor, 'value', backward=lambda v: f'HTML code:\n```\n{v}\n```')
