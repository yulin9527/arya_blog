## 添加配置文件

```python
TORTOISE_ORM = {
    "connections": {"default": "mysql://root:123456@127.0.0.1:3306/test"},
    "apps": {
        "models": {
            "models": ["tests.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
```

## 初始化

`aerich init -h`

```shell
Usage: aerich init [OPTIONS]

  Init config file and generate root migrate location.

Options:
  -t, --tortoise-orm TEXT  Tortoise-ORM config module dict variable, like
                           settings.TORTOISE_ORM.  [required]
  --location TEXT          Migrate store location.  [default: ./migrations]
  -s, --src_folder TEXT    Folder of the source, relative to the project root.
  -h, --help               Show this message and exit.
```

### 初始化配置文件和迁移位置

`aerich init -t app.settings.TORTOISE_ORM --location ./app/db/migrations`

```shell
Success create migrate location ./app/db/migrations
Success write config to pyproject.toml
```

## 初始化数据库
`aerich init-db`

```shell
Success create app migrate location app/db/migrations/User
Success generate schema for app "User"
```

## 更新模型并迁移
检测所有变动的模型并更新
`aerich migrate`

```shell
Success migrate 1_20231203231829_update.py
```

## 升级到最新版本
`aerich upgrade`

## 降级到指定版本
默认降级一次
`aerich downgrade`