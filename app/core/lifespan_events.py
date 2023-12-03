import contextlib
from fastapi import FastAPI
from tortoise import Tortoise

from app.settings import TORTOISE_ORM


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    """
    生命周期
    设置项目在启动时与停止时的动作
    :param app:
    :return:
    """
    print('开始执行')

    # 连接数据库
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    await Tortoise.generate_schemas()

    yield
    print('执行结束')
    await Tortoise.close_connections()
