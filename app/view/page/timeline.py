from functools import cache
from typing import List

from nicegui import ui
from nicegui import app as nice_app

from app import client
from app.db.schemas.page_schemas import TimeLineOUT


async def get_timeline(user_id=None):
    if not user_id:
        user_id = nice_app.storage.user['id']
    ret = await client.get(f'/timeline_user/{user_id}')
    if ret.status_code == 200:
        return ret.json()
    return []


async def time_line():
    data = await get_timeline()
    with ui.card().tight().classes('h-1/2 w-1/2').style(
            'position: absolute;margin:auto;top:0;right:0;bottom:0;left:0;opacity: 0.7;'):
        with ui.scroll_area().style('background-color:#CCFFCC').classes('w-full h-full border'):
            with ui.timeline(side='right', layout='dense'):
                for value in data:
                    ui.timeline_entry(value["body"], tag='---', title=value["title"], subtitle=value["dis_time"])
