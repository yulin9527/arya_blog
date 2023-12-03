from fastapi import Depends, Path, Response, Body

from app import HTTPException
from app.core.auth import get_current_active_user, get_password_hash
from app.db import User, Token
from app.db.schemas.user_schemas import UserOut


async def logout(response: Response, user: User = Depends(get_current_active_user)):
    """
    退出登录
    退出时删除浏览器cookie中的token值
    同时,将数据库中,用户的token的值设为空
    """
    response.delete_cookie(key='token')
    await Token.filter(pk=user.pk).update(token=None)
    return '操作成功'


async def user_info(user: User = Depends(get_current_active_user)):
    """
    获取用户个人信息
    """
    return await UserOut.from_tortoise_orm(user)


async def assign_info(user_id: int = Path(default=..., description='用户id', )):
    """
    获取指定用户的信息
    """
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(msg='请求的数据不存在')
    return await UserOut.from_tortoise_orm(user)


async def reset_password(user: User = Depends(get_current_active_user), new_password: str = Body()):
    """
    重置密码
    """
    new_password = get_password_hash(new_password)
    await User.filter(pk=user.pk).update(password=new_password)
    return '操作成功'
