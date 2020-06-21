from typing import TYPE_CHECKING

from py262.completion import NormalCompletion
from py262.utils.exceptions import Unreachable
from py262.value import Value

from .abstract_environment_record import AbstractEnvironmentRecord

if TYPE_CHECKING:
    from py262.completion import Completion


class ObjectEnvironmentRecord(AbstractEnvironmentRecord):
    '''https://tc39.es/ecma262/#sec-object-environment-records'''
    binding_object: Value
    with_environment: bool = False

    def has_binding(self, name: Value) -> 'Completion':
        raise NotImplementedError()

    def create_mutable_binding(self, name: Value,
                               deletable: Value) -> 'Completion':
        raise NotImplementedError()

    def create_immutable_binding(self, name: Value,
                                 strict: Value) -> 'Completion':
        raise Unreachable()

    def initialize_binding(self, name: Value, value: Value) -> 'Completion':
        raise NotImplementedError()

    def set_mutable_binding(self, name: Value, value: Value,
                            strict: Value) -> 'Completion':
        raise NotImplementedError()

    def get_binding_value(self, name: Value, strict: Value) -> 'Completion':
        raise NotImplementedError()

    def delete_binding(self, name: Value) -> 'Completion':
        raise NotImplementedError()

    def has_this_binding(self) -> 'Completion':
        return NormalCompletion(Value.false)

    def has_super_binding(self) -> 'Completion':
        return NormalCompletion(Value.false)

    def with_base_object(self) -> 'Completion':
        if self.with_environment:
            return NormalCompletion(self.binding_object)
        return NormalCompletion(Value.undefined)
