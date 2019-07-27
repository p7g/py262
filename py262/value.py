from typing import Union

import py262.environment

PRIMITIVE_TYPES = ('string', 'number', 'null', 'undefined', 'symbol')  # TODO


class Value:
    true: 'Value'
    false: 'Value'
    null: 'Value'
    undefined: 'Value'

    def is_primitive(self) -> bool:
        return type_of(self) in PRIMITIVE_TYPES


class BooleanValue(Value):
    def __init__(self, inner_value):
        assert isinstance(inner_value, bool)
        self.inner_value = inner_value


class NullValue(Value):
    pass


class UndefinedValue(Value):
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


def type_of(v: Union[Value, 'py262.environment.AbstractEnvironment']) -> str:
    if isinstance(v, BooleanValue):
        return 'boolean'
    if isinstance(v, NullValue):
        return 'null'
    if isinstance(v, UndefinedValue):
        return 'undefined'
    if isinstance(v, py262.environment.AbstractEnvironment):
        return 'environment'
    raise NotImplementedError()
