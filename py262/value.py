from dataclasses import dataclass
from typing import TypeVar, Union

from py262.completion import NormalCompletion, ThrowCompletion

PRIMITIVE_TYPES = ('string', 'number', 'null', 'undefined', 'symbol')  # TODO

T = TypeVar('T')

MaybeThrow = Union[NormalCompletion[T], ThrowCompletion]


class Value:
    true: 'BooleanValue'
    false: 'BooleanValue'
    null: 'NullValue'
    undefined: 'UndefinedValue'

    def is_primitive(self) -> bool:
        from py262.abstract_ops.value import type_of

        return type_of(self) in PRIMITIVE_TYPES


class BooleanValue(Value):
    def __init__(self, inner_value):
        assert isinstance(inner_value, bool)
        self.inner_value = inner_value


class NullValue(Value):
    pass


class UndefinedValue(Value):
    pass


@dataclass
class Property:
    enumerable: BooleanValue = Value.false
    configurable: BooleanValue = Value.false


@dataclass
class DataProperty(Property):
    value: Value = Value.undefined
    writable: BooleanValue = Value.false


@dataclass
class AccessorProperty(Property):
    get: Union['ObjectValue', UndefinedValue] = Value.undefined
    set: Union['ObjectValue', UndefinedValue] = Value.undefined


class ObjectValue(Value):
    def get_prototype_of(self) -> MaybeThrow[Union[NullValue, 'ObjectValue']]:
        pass

    def set_prototype_of(self, proto: Union[NullValue, 'ObjectValue']
                         ) -> MaybeThrow[BooleanValue]:
        pass

    def is_extensible(self) -> MaybeThrow[BooleanValue]:
        pass

    def prevent_extensions(self) -> MaybeThrow[BooleanValue]:
        pass


Value.true = BooleanValue(True)
Value.false = BooleanValue(False)
Value.null = NullValue()
Value.undefined = UndefinedValue()


def value(host_value) -> Value:
    if isinstance(host_value, bool):
        if host_value:
            return Value.true
        return Value.false
    return Value.undefined
