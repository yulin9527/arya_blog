from app.api.user_api.urls import login_router, user_router


def mian_router(fast_app):
    fast_app.include_router(login_router, tags=['登录'])
    fast_app.include_router(user_router, prefix='/user', tags=['用户'])

