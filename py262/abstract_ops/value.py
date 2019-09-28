from typing import TYPE_CHECKING, Union

from py262.environment import AbstractEnvironment
from py262.value import BooleanValue, NullValue, UndefinedValue

if TYPE_CHECKING:
    from py262.value import Value


def type_of(v: Union[Value, AbstractEnvironment]) -> str:
    if isinstance(v, BooleanValue):
        return 'boolean'
    if isinstance(v, NullValue):
        return 'null'
    if isinstance(v, UndefinedValue):
        return 'undefined'
    if isinstance(v, AbstractEnvironment):
        return 'environment'
    raise NotImplementedError()
