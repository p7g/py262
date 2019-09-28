from weakref import WeakSet


class schrodinger_property(property):
    '''A class property that cannot be changed once it has been observed'''
    def __init__(self, *args, **kwargs):
        self.observed = WeakSet()
        super().__init__(*args, **kwargs)

    def __get__(self, instance, *args, **kwargs):
        self.observed.add(instance)
        return super().__get__(instance, *args, **kwargs)

    def __set__(self, obj, value):
        assert obj not in self.observed
        return super().__set__(obj, value)
