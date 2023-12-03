from app.db.models import Abstract, Model, fields


class UserGroup(Abstract):
    name = fields.CharField(max_length=50, description='用户组名称')
    user: fields.ReverseRelation["User"]


class User(Abstract):
    account = fields.CharField(max_length=50, index=True, unique=True, description='账号', null=True)
    username = fields.CharField(max_length=50, description='用户名_昵称', null=True, default=None)
    password = fields.CharField(max_length=100, description='密码')
    phone = fields.CharField(max_length=15, index=True, description='手机号', null=True, default=None)
    email = fields.CharField(max_length=30, index=True, description='邮箱', null=True, default=None)
    signature = fields.CharField(max_length=100, description='签名', null=True, default=None)
    avatar = fields.CharField(max_length=100, description='头像地址', null=True, default=None)
    sex = fields.CharField(max_length=20, description='性别', default='保密')

    # 不生产实际字段,仅作为编辑器代码提示
    token: fields.ReverseRelation["Token"]
    group: fields.ForeignKeyNullableRelation[UserGroup] = fields.ForeignKeyField('User.User',
                                                                                 related_name='user', null=True)

    class Meta:
        table = 'users'


class Token(Model):
    user: fields.ForeignKeyNullableRelation[User] = fields.ForeignKeyField('User.User', related_name='token',
                                                                           null=True)
    token = fields.CharField(max_length=255, null=True)
