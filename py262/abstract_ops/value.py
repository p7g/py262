from typing import TYPE_CHECKING, Union

from py262.environment import AbstractEnvironmentRecord
from py262.value import (BooleanValue, NullValue, ObjectValue, StringValue,
                         UndefinedValue)

if TYPE_CHECKING:
    from py262.value import Value  # noqa: W0611


def type_of(v: Union['Value', AbstractEnvironmentRecord]) -> str:
    if isinstance(v, BooleanValue):
        return 'boolean'
    if isinstance(v, NullValue):
        return 'null'
    if isinstance(v, UndefinedValue):
        return 'undefined'
    if isinstance(v, StringValue):
        return 'string'
    if isinstance(v, ObjectValue):
        return 'object'
    if isinstance(v, AbstractEnvironmentRecord):
        return 'environment'
    raise ValueError(v)
