import enum


class CompletionType(enum.Enum):
    NORMAL = 'normal'
    BREAK = 'break'
    CONTINUE = 'continue'
    RETURN = 'return'
    THROW = 'throw'


class Completion:
    def __init__(self, type_, value, target):
        self.type = type_
        self.value = value
        self.target = target

    def is_abrupt(self) -> bool:
        return self.type != CompletionType.NORMAL


class NormalCompletion(Completion):
    def __init__(self, value):
        super().__init__(CompletionType.NORMAL, value, None)


class ThrowCompletion(Completion):
    def __init__(self, value):
        super().__init__(CompletionType.THROW, value, None)
