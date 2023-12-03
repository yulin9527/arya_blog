import math

from fastapi import Query
from pydantic import BaseModel
from starlette import status
from tortoise.queryset import QuerySet
from typing import TypeVar, Sequence

from app import HTTPException

T = TypeVar("T")


class PagePydantic(BaseModel):
    """分页模型"""
    total: int  # 数据量总数
    total_pages: int  # 总页码
    page: int  # 当前页码
    size: int  # 每页显示数据量

    data: Sequence[T]


class Params(BaseModel):
    """传参"""
    # 设置默认值为1，不能够小于1
    page: int = Query(1, ge=1, description="页码")
    # 设置默认值为10，最大为100
    size: int = Query(10, gt=0, le=200, description="每页显示数量")
    order_by: str = Query(None, max_length=32, description="Sort key")  # 默认值None表示选传


async def pagination(pydantic_model, query_set: QuerySet, params: Params, callback=None):
    """分页响应"""
    page: int = params.page
    size: int = params.size
    order_by: str = params.order_by
    total = await query_set.count()

    # 通过总数和每页数量计算出总页数
    total_pages = math.ceil(total / size)

    if page > total_pages and total:  # 排除查询集为空时报错，即total=0时
        return HTTPException(msg="页数输入有误", code=status.HTTP_400_BAD_REQUEST)

    # 排序后分页
    if order_by:
        query_set = query_set.order_by(order_by)
    # 分页
    query_set = query_set.offset((page - 1) * size)  # 页数 * 页面大小=偏移量
    query_set = query_set.limit(size)

    if callback:
        """对查询集操作"""
        query_set = await callback(query_set)

    data = await pydantic_model.from_queryset(query_set)

    return PagePydantic(
        total=total,
        total_pages=total_pages,
        page=page,
        size=size,
        data=data
    )
