from dataclasses import dataclass
from typing import Union

from py262.utils import classproperty, singleton

PRIMITIVE_TYPES = ('string', 'number', 'null', 'undefined', 'symbol')  # TODO


class Value:
    @classproperty
    @singleton
    def true(cls):
        return BooleanValue(True)

    @classproperty
    @singleton
    def false(cls):
        return BooleanValue(False)

    @classproperty
    @singleton
    def null(cls):
        return NullValue()

    @classproperty
    @singleton
    def undefined(cls):
        return UndefinedValue()

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
    def get_prototype_of(self):
        pass

    def set_prototype_of(self, proto):
        pass

    def is_extensible(self):
        pass

    def prevent_extensions(self):
        pass


def value(host_value) -> Value:
    if isinstance(host_value, bool):
        if host_value:
            return Value.true
        return Value.false
    return Value.undefined
