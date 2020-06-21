from dataclasses import dataclass
from typing import Union

from py262.completion import Completion
from py262.utils import classproperty, singleton

PRIMITIVE_TYPES = ('string', 'boolean', 'number', 'null', 'undefined',
                   'symbol')

UNDEFINED = object()


class Value:
    @classproperty
    @singleton
    def true(cls) -> 'BooleanValue':
        return BooleanValue(True)

    @classproperty
    @singleton
    def false(cls) -> 'BooleanValue':
        return BooleanValue(False)

    @classproperty
    @singleton
    def null(cls) -> 'NullValue':
        return NullValue()

    @classproperty
    @singleton
    def undefined(cls) -> 'UndefinedValue':
        return UndefinedValue()

    def is_primitive(self) -> bool:
        from py262.abstract_ops.value import type_of

        return type_of(self) in PRIMITIVE_TYPES


class BooleanValue(Value):
    def __init__(self, inner_value: bool):
        assert isinstance(inner_value, bool)
        self.inner_value = inner_value


class NullValue(Value):
    pass


class UndefinedValue(Value):
    pass


class StringValue(Value):
    def __init__(self, inner_value: str):
        assert isinstance(inner_value, str)
        self.inner_value = inner_value

    def __hash__(self):
        return hash(self.inner_value)


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
    def get_prototype_of(self) -> Completion:
        pass

    def set_prototype_of(self, proto: Value) -> Completion:
        pass

    def is_extensible(self) -> Completion:
        pass

    def prevent_extensions(self) -> Completion:
        pass


def value(host_value=UNDEFINED) -> Value:
    if isinstance(host_value, bool):
        if host_value:
            return Value.true
        return Value.false
    if isinstance(host_value, str):
        return StringValue(host_value)
    if host_value is None:
        return Value.null
    if host_value is UNDEFINED:
        return Value.undefined
    raise ValueError(host_value)
