import enum
from typing import Optional, Union

from py262.reference import Reference
from py262.value import Value


class CompletionType(enum.Enum):
    NORMAL = 'normal'
    BREAK = 'break'
    CONTINUE = 'continue'
    RETURN = 'return'
    THROW = 'throw'


class Completion:
    type: CompletionType
    value: Optional[Union[Value, Reference]]
    target: Optional[Value]

    def __init__(self, type_: CompletionType,
                 value: Optional[Union[Value, Reference]],
                 target: Optional[Value]):
        self.type = type_
        self.value = value
        self.target = target

    def is_abrupt(self) -> bool:
        return self.type != CompletionType.NORMAL


class NormalCompletion(Completion):
    def __init__(self, value: Optional[Union[Value, Reference]]):
        super().__init__(CompletionType.NORMAL, value, None)


class ThrowCompletion(Completion):
    def __init__(self, value: Optional[Union[Value, Reference]]):
        super().__init__(CompletionType.THROW, value, None)


def update_empty(completion, value: Value) -> Completion:
    assert completion.value is not None if completion.type in [
        CompletionType.RETURN,
        CompletionType.THROW,
    ] else True

    if completion.value is not None:
        return completion
    return Completion(completion.type, value, completion.target)
