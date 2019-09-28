import enum
from typing import TYPE_CHECKING, Generic, Optional, TypeVar

if TYPE_CHECKING:
    from py262.value import Value  # noqa: W0611


class CompletionType(enum.Enum):
    NORMAL = 'normal'
    BREAK = 'break'
    CONTINUE = 'continue'
    RETURN = 'return'
    THROW = 'throw'


T = TypeVar('T')


class Completion(Generic[T]):
    type: CompletionType
    value: Optional[T]
    target: Optional['Value']

    def __init__(self, type_: CompletionType, value: Optional[T],
                 target: Optional['Value']):
        self.type = type_
        self.value = value
        self.target = target

    def is_abrupt(self) -> bool:
        return self.type != CompletionType.NORMAL


class NormalCompletion(Completion[T]):
    def __init__(self, value: Optional[T]):
        super().__init__(CompletionType.NORMAL, value, None)


class ThrowCompletion(Completion['Value']):
    def __init__(self, value: Optional['Value']):
        super().__init__(CompletionType.THROW, value, None)
