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
    def __init__(self, type_: CompletionType, value: Optional[Value], target: Optional[Value]):
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


def update_empty(completion, value: Value) -> Completion:
    assert completion.value is not None if completion.type in [
        CompletionType.RETURN, CompletionType.THROW,
    ] else True

    if completion.value is not None:
        return completion
    return Completion(completion.type, value, completion.target)
