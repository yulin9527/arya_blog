import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv

# 读取.env文件数据
load_dotenv(find_dotenv(), override=True)

# 开发模式配置
DEBUG: bool = True

# 项目文档
TITLE: str = 'Arya_api'
SUMMARY: str = 'api接口完善'
DESCRIPTION: str = "更多FastAPI知识"
# 文档地址 默认为docs 生产环境关闭 None
DOCS_URL: str = "/api/docs"
# 文档关联请求数据接口
OPENAPI_URL: str = "/api/openapi.json"
# redoc 文档
REDOC_URL: Optional[str] = "/api/redoc"

# token过期时间 分钟
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
# 生成token的加密算法
ALGORITHM: str = "HS256"
# JWT令牌随机密钥,用于对jwt令牌进行签名  生成方式 openssl rand -hex 32
SECRET_KEY: str = os.getenv('SECRET_KEY', 'f09b6e3fa7b71df48c922b20d3c225fc43fd91c23536e5291c64175db1b2fd88')

# 项目根路径
BASE_PATH: str = os.path.dirname(os.path.abspath(__file__))

# 数据库设置
TORTOISE_ORM = {
    "connections": {
        "pgsql": {
            'engine': 'tortoise.backends.asyncpg',
            "credentials": {
                'host': os.getenv('BASE_HOST', '127.0.0.1'),
                'user': os.getenv('BASE_USER', 'postgres'),
                'password': os.getenv('BASE_PASSWORD', '12345678'),
                'port': os.getenv('BASE_PORT', 5432),
                'database': os.getenv('BASE_DB', 'fast_nice'),
            }
        },
    },
    "apps": {
        "User": {"models": [
            "app.db.models.users"
            # "aerich.models"
        ],
            "default_connection": "pgsql"},
        # "db2": {"models": ["models.db2"], "default_connection": "db2"},
        # "db3": {"models": ["models.db3"], "default_connection": "db3"}
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
    "generate_schemas": True
}

# redis配置
REDIS_HOST: str = "127.0.0.1"
REDIS_PASSWORD: str = ""
REDIS_DB: int = 0
REDIS_PORT: int = 6379
REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"
REDIS_TIMEOUT: int = 5  # redis连接超时时间

CASBIN_MODEL_PATH: str = "./resource/rbac_model.conf"

# 允许访问的域名
origins = ["http://127.0.0.1"]
