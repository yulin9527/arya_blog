from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.fields import Field

from app.core.utils.tools import _time_str
from app.db.models.pages import TimeLine

TimeLineIN = pydantic_model_creator(TimeLine, name='timeline_in', exclude=('is_delete', 'created', 'modified', 'id'))


# TimeLine_OUT = pydantic_model_creator(TimeLine, name='timeline_out')


class TimeLineOUT(pydantic_model_creator(TimeLine, name="timeline_out")):
    # group: Union[UserGroupPydantic, None]
    # show_time = '123'
    pass
