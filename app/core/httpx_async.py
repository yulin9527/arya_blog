import typing

from fastapi import FastAPI
from httpx import AsyncClient, Response, USE_CLIENT_DEFAULT
from httpx._client import UseClientDefault
from httpx._types import URLTypes, RequestContent, RequestData, RequestFiles, QueryParamTypes, HeaderTypes, CookieTypes, \
    AuthTypes, TimeoutTypes, RequestExtensions
from nicegui import ui

from nicegui import app as nice_app


class AsyncHttpX:
    def __init__(self, app: FastAPI):
        self.app = app

    async def post(self, url: URLTypes,
                   *,
                   content: typing.Optional[RequestContent] = None,
                   data: typing.Optional[RequestData] = None,
                   files: typing.Optional[RequestFiles] = None,
                   json: typing.Optional[typing.Any] = None,
                   params: typing.Optional[QueryParamTypes] = None,
                   headers: typing.Optional[HeaderTypes] = None,
                   cookies: typing.Optional[CookieTypes] = None,
                   auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
                   follow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
                   timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
                   extensions: typing.Optional[RequestExtensions] = None, ) -> Response:
        async with AsyncClient(app=self.app, base_url='http://test') as ac:
            if not headers:
                headers = dict()
            headers['Authorization'] = nice_app.storage.user.setdefault('token', '')
            response: Response = await ac.post(url=url, content=content, data=data, files=files, json=json,
                                               params=params, headers=headers, cookies=cookies, auth=auth,
                                               follow_redirects=follow_redirects,
                                               timeout=timeout, extensions=extensions)
            # if response.status_code == 400:
            #     ui.open('/')
            return response
