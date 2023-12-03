import hashlib
import uuid
from datetime import datetime
from random import randrange


def _time_str(time_str):
    """
    将时间格式转化为字符串
    :param time_str:
    :return:
    """
    return datetime.strftime(time_str, '%Y-%m-%d %H:%M:%S')


def _str_time(time_str):
    """
    将字符串转化为时间
    :param time_str: 
    :return: 
    """""
    return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')


def code_number(length: int):
    """
    随机数字验证码
    :param length: 长度
    :return: str
    """
    code = ""
    for i in range(length):
        ch = chr(randrange(ord('0'), ord('9') + 1))
        code += ch

    return code


def random_str():
    """
    唯一随机字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid4()).encode(encoding='UTF-8')).hexdigest()
    return only
