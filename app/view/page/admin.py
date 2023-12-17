import httpx
import pytest
from httpx import AsyncClient
from nicegui import ui
from nicegui import app as nice_app

from app import client, fast_app


async def on_log(account, password, button):
    print(account, password)
    user = await client.post('/user/me', data={'username': account, "password": password})
    if user.status_code == 200:
        print(user.json())
        # ui.open('/')
    print(user.status_code)
