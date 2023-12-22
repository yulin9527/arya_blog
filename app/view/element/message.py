import os
from typing import List, Tuple
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from nicegui import context, ui

OPENAI_API_KEY = os.getenv('OPENAI_KEY', )


@ui.refreshable
def chat_messages(messages, thinking) -> None:
    for name, text in messages:
        ui.chat_message(text=text, name=name, sent=name == 'arya')
    if thinking:
        ui.spinner(size='3rem').classes('self-center')
    if context.get_client().has_socket_connection:
        ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')


def openai_msg():
    llm = ConversationChain(llm=ChatOpenAI(model_name='gpt-3.5-turbo-1106', openai_api_key=OPENAI_API_KEY))

    messages: List[Tuple[str, str]] = []
    thinking: bool = False

    async def send() -> None:
        nonlocal thinking
        message = text.value
        if not message:
            return
        messages.append(('arya', text.value))
        thinking = True
        text.value = ''
        chat_messages.refresh()

        response = await llm.arun(message)
        messages.append(('娜娜', response))
        thinking = False
        chat_messages.refresh()

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    ui.add_head_html(f'<style>{anchor_style}</style>')

    ui.query('.q-page').classes('flex')
    ui.query('.nicegui-content').classes('w-full')

    with ui.tabs().classes('w-full') as tabs:
        chat_tab = ui.tab('Chat')
    with ui.tab_panels(tabs, value=chat_tab).classes('w-full max-w-2xl mx-auto flex-grow items-stretch'):
        with ui.tab_panel(chat_tab).classes('items-stretch'):
            chat_messages(messages, thinking)

    with ui.row().classes('w-full no-wrap items-center'):
        placeholder = 'message' if OPENAI_API_KEY != 'not-set' else \
            'Please provide your OPENAI key in the Python script first!'
        text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3') \
            .classes('w-full self-center').on('keydown.enter', send)
