from typing import Union

from py262 import environment
from py262.value import Value, type_of

VALID_BASE_TYPES = ('undefined', 'object', 'boolean', 'string', 'symbol',
                    'number')
VALID_REFERENCED_NAME_TYPES = ('string', 'symbol')


class Reference:
    base: Union[Value, 'environment.AbstractEnvironment']
    referenced_name: Value
    is_strict: Value

    def __init__(self, base: Union[Value, 'environment.AbstractEnvironment'],
                 referenced_name: Value, is_strict: Value):
        assert type_of(base) in VALID_BASE_TYPES \
            or isinstance(base, environment.AbstractEnvironment)
        assert type_of(referenced_name) in VALID_REFERENCED_NAME_TYPES
        assert type_of(is_strict) == 'boolean'

        self.base = base
        self.referenced_name = referenced_name
        self.is_strict = is_strict


class SuperReference(Reference):
    this_value: Value

    def __init__(self, this_value: Value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.this_value = this_value
