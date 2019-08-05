class singleton:
    def __init__(self, fn):
        self.fn = fn
        self.value = None

    def __call__(self, *args, **kwargs):
        if self.value is not None:
            return self.value
        self.value = self.fn(*args, **kwargs)
        return self.value
