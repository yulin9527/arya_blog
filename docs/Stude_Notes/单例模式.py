import threading


class TaskManager:

    def __init__(self):
        # 显示化窗口
        pass

    def display_processes(self):
        """
        显示进程
        :return: 
        """""
        pass

    def display_services(self):
        """
        显示服务
        :return: 
        """""
        pass


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls

    return inner()


class Single(object):
    _instance = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Single, '_instance'):
            with Single._instance:
                if not hasattr(Single, '_instance'):
                    Single._instance = object.__new__(cls)
        return Single._instance

    def __init__(self, name=None, *, age=18):
        self.name = name
        print(id(self), self.name)


def task(arg):
    obj = Single(arg)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[str(i), ])
    t.start()
