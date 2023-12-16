from app.core.utils.tools import _time_str
from app.db import User
from app.db.models import Abstract, Model, fields


class TimeLine(Abstract):
    user: fields.ForeignKeyNullableRelation[User] = fields.ForeignKeyField('User.User', related_name='time_line',
                                                                           null=True)
    title = fields.CharField(max_length=50, description='标题', null=True, default=None)
    body = fields.CharField(max_length=50, description='内容', null=True, default=None)
    subtitle = fields.CharField(max_length=50, description='副标题', null=True, default=None)
    icon = fields.CharField(max_length=50, description='图标', null=True, default=None)
    show_time = fields.DatetimeField(null=True, description='显示时间')

    def dis_time(self) -> str:
        return _time_str(self.show_time)

    class PydanticMeta:
        # Let's include two callables as computed columns
        computed = ("dis_time", )
