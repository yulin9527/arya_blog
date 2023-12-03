from fastapi import Body, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from app.core.auth import get_password_hash, create_access_token, authenticate_user
from app.core.exception import HTTPException
from app.db.models.users import User, Token
from app.db.schemas.user_schemas import Login, UserOut


async def register(user: Login = Body(), code: str = Body(default=None), ):
    if await User.get_or_none(account=user.account):
        raise HTTPException(msg=f'{user.account} 用户已存在')
    # if user.phone:
    #     # 注册阶段如果提供手机号,需对手机号进行判断,
    #     if await User.get_or_none(phone=user.phone):
    #         raise HTTPException(msg=f'{user.phone} 手机号已绑定')
    #     else:
    #         data = await server.Redis_Check.get(name=f"{user.phone}__1")
    #         print(data)
    #         if not data == code:
    #             raise HTTPException(msg='验证码不正确')
    #         await server.Redis_Check.delete(f"{user.phone}__1")

    user.password = get_password_hash(user.password)
    user_obj = await User.create(**user.model_dump())
    return await UserOut.from_tortoise_orm(user_obj)


async def login(user_data: OAuth2PasswordRequestForm = Depends()):
    if user := await authenticate_user(account=user_data.username, password=user_data.password):
        # 创建token
        access_token = create_access_token(data={'sub': user.account})
        await Token.update_or_create(defaults={'token': access_token}, user=user)
        # 将token写入到浏览器cookie中
        response = Response()
        response.set_cookie(key='token', value=access_token)
        return response
    else:
        raise HTTPException(msg='用户名或密码错误')
