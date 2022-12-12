class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'exist'):
            cls.exist = super().__new__(cls, *args, **kwargs)
        return cls.exist


class Counter:
    pass


class GlobalCounter(Singleton, Counter):
    pass


gc1 = GlobalCounter()
gc2 = GlobalCounter()
print(id(gc1) == id(gc2))
