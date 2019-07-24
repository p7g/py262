class schrodinger_property(property):  # pylint: disable=invalid-name
    '''A class property that cannot be changed once it has been observed'''
    observed = False

    def __get__(self, *args, **kwargs):
        self.observed = True
        return super().__get__(*args, **kwargs)

    def __set__(self, obj, value):
        assert not self.observed
        return super().__set__(obj, value)
