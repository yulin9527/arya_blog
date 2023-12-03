import os
import httpx
import uvicorn

from fastapi import FastAPI
from nicegui import ui
from starlette.testclient import TestClient
from fastapi.staticfiles import StaticFiles
from app import FastAPIException
from app.api.routers import mian_router
from app.core.lifespan_events import lifespan
from app.core.middleware import middleware_init
from app.settings import BASE_PATH

fast_app = FastAPI(lifespan=lifespan)

# 中间件设置
middleware_init(fast_app)

# 挂接路由
mian_router(fast_app)

# 自定义异常捕获
FastAPIException(fast_app)

# 接口调用
client: httpx.Client = TestClient(fast_app)

# 静态文件
fast_app.mount('/static', StaticFiles(directory=os.path.join(BASE_PATH, 'static')), name='static')

# 挂接 nicegui 应用
ui.run_with(fast_app, title='羽林')

if __name__ == '__main__':
    uvicorn.run(app='main:fast_app', port=8010, reload=True)
