def emptyinit(self):
    pass


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'exist'):
            cls.exist = super().__new__(cls, *args, **kwargs)
        else:
            cls.__init__ = emptyinit
        return cls.exist


class Counter:
    def __init__(self):
        print('Hello from counter')


class GlobalCounter(Singleton, Counter):
    def __init__(self):
        print("Hello from GC")


gc1 = GlobalCounter()
gc2 = GlobalCounter()
print(id(gc1) == id(gc2))
