import enum
from typing import TYPE_CHECKING

from py262.completion import NormalCompletion, ThrowCompletion
from py262.value import Value, value

from .declarative_environment_record import DeclarativeEnvironmentRecord

if TYPE_CHECKING:
    from py262.completion import Completion


class ThisBindingStatus(enum.Enum):
    LEXICAL = 'lexical'
    INITIALIZED = 'initialized'
    UNINITIALIZED = 'uninitialized'


class FunctionEnvironmentRecord(DeclarativeEnvironmentRecord):
    this_value: Value
    this_binding_status: ThisBindingStatus
    function_object: Value
    home_object: Value
    new_target: Value

    def bind_this_value(self, val: Value) -> 'Completion':
        assert self.this_binding_status != ThisBindingStatus.LEXICAL
        if self.this_binding_status == ThisBindingStatus.INITIALIZED:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        self.this_value = val
        self.this_binding_status = ThisBindingStatus.INITIALIZED
        return NormalCompletion(val)

    def has_this_binding(self) -> Value:
        return value(self.this_binding_status != ThisBindingStatus.LEXICAL)

    def has_super_binding(self) -> 'Completion':
        if self.this_binding_status == ThisBindingStatus.LEXICAL:
            return NormalCompletion(Value.false)
        return NormalCompletion(value(self.home_object is not Value.undefined))

    def get_this_binding(self) -> 'Completion':
        assert self.this_binding_status != ThisBindingStatus.LEXICAL
        if self.this_binding_status == ThisBindingStatus.UNINITIALIZED:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        return NormalCompletion(self.this_value)

    # FIXME
    # def get_super_base(self) -> 'Completion':
    #     if self.home_object is Value.undefined:
    #         return NormalCompletion(Value.undefined)
    #     assert type_of(self.home_object) == 'object'
    #     completion = self.home_object.get_prototype_of()
    #     if completion.is_abrupt():
    #         return completion
    #     return NormalCompletion(completion.value)
