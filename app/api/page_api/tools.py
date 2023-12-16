from fastapi import Body, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from app.core.auth import get_password_hash, create_access_token, authenticate_user, get_current_active_user
from app.core.exception import HTTPException
from app.db.models.pages import TimeLine
from app.db.models.users import User, Token
from app.db.schemas.page_schemas import TimeLineIN, TimeLineOUT
from app.db.schemas.user_schemas import Login, UserOut


async def get_timeline(user_id):
    obj = TimeLine.filter(user_id=user_id, is_delete=False).order_by('show_time')
    return await TimeLineOUT.from_queryset(obj)


async def set_timeline(user: User = Depends(get_current_active_user), timeline: TimeLineIN = Body()):
    obj = await TimeLine.create(**timeline.model_dump(), user_id=user.pk)
    return await TimeLineOUT.from_tortoise_orm(obj)


async def login_for_access_token(user_data: OAuth2PasswordRequestForm = Depends()):
    if user := await authenticate_user(account=user_data.username, password=user_data.password):
        # 创建token
        access_token = create_access_token(data={'sub': user.account})
        await Token.update_or_create(defaults={'token': access_token}, user=user)
        return {"token_type": "bearer", "access_token": access_token}
    else:
        raise HTTPException(msg='用户名或密码错误')
