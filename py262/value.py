PRIMITIVE_TYPES = ('string', 'number', 'null', 'undefined', 'symbol')  # TODO


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
