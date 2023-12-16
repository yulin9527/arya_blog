from typing import Union

from fastapi import APIRouter, Depends

from app.api.page_api.tools import get_timeline, set_timeline
from app.api.user_api.login import register, login_for_access_token
from app.api.user_api.user import *
from app.core.auth import get_current_active_user

page_router = APIRouter(
    responses={404: {"description": "找不到"}},
)

page_router.get('/timeline_user/{user_id}')(get_timeline)
page_router.post('/timeline_user')(set_timeline)
# login_router.post('/register', summary='用户注册')(register)
# login_router.post('/token', summary='获取 token')(login_for_access_token)
# # login_router.post('/send_sms', summary='获取验证码')(send_sms)
#
# user_router.delete('/logout', summary='退出登录')(logout)
# user_router.get('/me', summary='获取个人信息', response_model=UserOut)(user_info)
# # user_router.get('/all', summary='获取所有用户信息', response_model=List[UserOut])(user_all)
# user_router.get('/{user_id}', summary='获取指定用户信息', response_model=Union[UserOut])(assign_info)
# user_router.put('/me/pwd', summary='重置密码')(reset_password)
