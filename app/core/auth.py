from datetime import datetime, timedelta
from typing import Union
from fastapi import Cookie, Response, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from app import HTTPException
from app.db import User, Token
from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    """
    校验密码
    :param plain_password: 原密码
    :param hashed_password: 哈希后的密码
    :return: bool  校验成功返回True,反之False
    """

    # noinspection PyBroadException
    # try:
    return pwd_context.verify(plain_password, hashed_password)
    # except Exception:
    #     return False


def get_password_hash(password):
    """
    哈希来自用户的密码
    :param password: 原密码
    :return: 哈希后的密码
    """
    return pwd_context.hash(password)


async def authenticate_user(account, password) -> Union[User, bool]:
    """
    校验用户密码
    :param account: 账号
    :param password: 密码
    :return:
    """
    user = await User.get_or_none(account=account, is_delete=False)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    """
    访问令牌,创建token
    :param data: 需要JWT令牌加密的数据
    :param expires_delta: 令牌有效期
    :return: token
    """
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=expires_delta)
    # 添加失效时间
    to_encode.update({"exp": expire})
    # SECRET_KEY:密钥
    # ALGORITHM:令牌签名算法
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def check_jwt_token(token: str = Cookie(default='')) -> Union[User, None]:
    """
    验证token
    :param token: 浏览器取到的一个字符串的值
    :return: 用户
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(code=status.HTTP_401_UNAUTHORIZED, msg='token验证失败')
    account: str = payload.get('sub')
    if user := await User.get_or_none(account=account):
        if datetime.now() + timedelta(minutes=60 * 12) > datetime.fromtimestamp(payload.get('exp')):
            # 过期时间小于10分钟,刷新token
            access_token = create_access_token(data={'sub': user.username})
            response = Response()
            response.set_cookie(key='token', value=access_token)
            await Token.update_or_create(defaults={'token': access_token}, user=user)
        return user
    else:
        raise HTTPException(code=status.HTTP_401_UNAUTHORIZED, msg='token验证成功,用户查找失败')


async def get_current_active_user(current_user: User = Depends(check_jwt_token)):
    # TODO 用户状态判断预留
    # if current_user.disabled:
    #     raise HTTPException(code=status.HTTP_401_UNAUTHORIZED,msg='权限问题,无法登录')
    return current_user


async def check_admin_token(user: User = Depends(check_jwt_token)):
    """
    验证用户是否为管理员
    :param user:
    :return:
    """
    # if user.type == UserType.admin:
    #     return user
    # else:
    #     raise HTTPException(code=status.HTTP_401_UNAUTHORIZED, msg='token验证失败,用户非管理员')
