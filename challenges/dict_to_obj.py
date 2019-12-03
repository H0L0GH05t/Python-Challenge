"""
Implement a class that can convert a Python dictionary into an object.

    {
        'a': 1,
        'b': {
            'c': 2,
        },
    }

    obj.a    # should return 1
    obj.b.c  # should return 2

"""


class DictToObj:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if type(value) == dict:
                    setattr(self, key, DictToObj(value))
                else:
                    setattr(self, key, value)
        elif args:
            for item in args:
                if type(item) == dict:
                    for key, value in item.items():
                        if type(value) == dict:
                            setattr(self, key, DictToObj(value))
                        else:
                            setattr(self, key, value)
