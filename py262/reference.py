from typing import TYPE_CHECKING, Union

from py262.abstract_ops.value import type_of
from py262.environment import EnvironmentRecord

if TYPE_CHECKING:
    from py262.value import Value

VALID_BASE_TYPES = ('undefined', 'object', 'boolean', 'string', 'symbol',
                    'number')
VALID_REFERENCED_NAME_TYPES = ('string', 'symbol')


class Reference:
    base: Union[Value, EnvironmentRecord]
    referenced_name: Value
    is_strict: Value

    def __init__(self, base: Union[Value, EnvironmentRecord],
                 referenced_name: Value, is_strict: Value):
        assert type_of(base) in VALID_BASE_TYPES \
            or isinstance(base, EnvironmentRecord)
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
