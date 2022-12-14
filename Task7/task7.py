def emptyinit(self):
    pass


class Singleton:
    new = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'exist'):
            cls.exist = super().__new__(cls, *args, **kwargs)
            Singleton.new = True
        else:
            cls.__init__ = emptyinit
        return cls.exist


class Counter:
    def __init__(self):
        print('Hello')


class GlobalCounter(Singleton, Counter):
    pass


gc1 = GlobalCounter()
gc2 = GlobalCounter()
print(id(gc1) == id(gc2))
