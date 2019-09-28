from typing import TYPE_CHECKING

from py262.completion import NormalCompletion
from py262.utils.exceptions import Unreachable
from py262.value import Value

from .abstract_environment import AbstractEnvironment

if TYPE_CHECKING:
    from py262.completion import Completion


class ObjectEnvironment(AbstractEnvironment):
    '''https://tc39.es/ecma262/#sec-object-environment-records'''
    binding_object: Value
    with_environment: bool

    def has_binding(self, name) -> 'Completion':
        raise NotImplementedError()

    def create_mutable_binding(self, name, deletable: Value) -> 'Completion':
        raise NotImplementedError()

    def create_immutable_binding(self, name, strict: Value) -> 'Completion':
        raise Unreachable()

    def initialize_binding(self, name, value: Value) -> 'Completion':
        raise NotImplementedError()

    def set_mutable_binding(self, name, value: Value,
                            strict: Value) -> 'Completion':
        raise NotImplementedError()

    def get_binding_value(self, name, strict: Value) -> 'Completion':
        raise NotImplementedError()

    def delete_binding(self, name) -> 'Completion':
        raise NotImplementedError()

    def has_this_binding(self) -> 'Completion':
        return NormalCompletion(Value.false)

    def has_super_binding(self) -> 'Completion':
        return NormalCompletion(Value.false)

    def with_base_object(self) -> 'Completion':
        if self.with_environment:
            return NormalCompletion(self.binding_object)
        return NormalCompletion(Value.undefined)
