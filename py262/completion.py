import enum
from typing import Optional

from py262.value import Value


class CompletionType(enum.Enum):
    NORMAL = 'normal'
    BREAK = 'break'
    CONTINUE = 'continue'
    RETURN = 'return'
    THROW = 'throw'


class Completion:
    type: CompletionType
    value: Optional[Value]
    target: Optional[Value]

    def __init__(self, type_: CompletionType, value: Optional[Value],
                 target: Optional[Value]):
        self.type = type_
        self.value = value
        self.target = target

    def is_abrupt(self) -> bool:
        return self.type != CompletionType.NORMAL


class NormalCompletion(Completion):
    def __init__(self, value: Optional[Value]):
        super().__init__(CompletionType.NORMAL, value, None)


class ThrowCompletion(Completion):
    def __init__(self, value: Optional[Value]):
        super().__init__(CompletionType.THROW, value, None)
