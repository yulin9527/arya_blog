from typing import Union
from tortoise.contrib.pydantic import pydantic_model_creator

from app.db import UserGroup, User


Login = pydantic_model_creator(User, name='login', include=('account', 'username', 'password', 'phone'))
UserGroupPydantic = pydantic_model_creator(UserGroup, name='user_group', include=('name', 'id'))


class UserOut(pydantic_model_creator(User, name="user_out", exclude=('password',))):
    group: Union[UserGroupPydantic, None]
