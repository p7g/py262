from typing import List

from py262.completion import Completion, NormalCompletion, ThrowCompletion
from py262.value import Value, value

from .declarative_environment_record import DeclarativeEnvironmentRecord
from .environment_record import EnvironmentRecord
from .object_environment_record import ObjectEnvironmentRecord


class GlobalEnvironmentRecord(EnvironmentRecord):
    object_record: ObjectEnvironmentRecord
    global_this_value: Value
    declarative_record: DeclarativeEnvironmentRecord
    var_names: List[Value]

    def has_binding(self, name: Value) -> Completion:
        if self.declarative_record.has_binding(name).value is Value.true:
            return NormalCompletion(Value.true)
        return self.object_record.has_binding(name)

    def create_mutable_binding(self, name: Value,
                               deletable: Value) -> Completion:
        if self.declarative_record.has_binding(name).value is Value.true:
            return ThrowCompletion(value('new TypeError'))  # FIXME
        return self.declarative_record.create_mutable_binding(name, deletable)

    def create_immutable_binding(self, name: Value,
                                 strict: Value) -> Completion:
        if self.declarative_record.has_binding(name) is Value.true:
            return ThrowCompletion(value('new TypeError'))  # FIXME
        return self.declarative_record.create_immutable_binding(name, strict)

    def initialize_binding(self, name: Value, val: Value) -> Completion:
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.initialize_binding(name, val)
        assert 'binding must be in object environment if it exists'
        return self.object_record.initialize_binding(name, val)

    def set_mutable_binding(self, name: Value, val: Value,
                            strict: Value) -> Completion:
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.set_mutable_binding(
                name, val, strict)
        return self.object_record.set_mutable_binding(name, val, strict)

    def get_binding_value(self, name: Value, strict: Value) -> Completion:
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.get_binding_value(name, strict)
        return self.object_record.get_binding_value(name, strict)

    # https://tc39.es/ecma262/#sec-global-environment-records-deletebinding-n
    def delete_binding(self, name: Value) -> Completion:
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.delete_binding(name)
        raise NotImplementedError()

    def has_this_binding(self) -> Value:
        return Value.true

    def has_super_binding(self) -> Completion:
        return NormalCompletion(Value.false)

    def with_base_object(self) -> Completion:
        return NormalCompletion(Value.undefined)

    def get_this_binding(self) -> Completion:
        return NormalCompletion(self.global_this_value)

    def has_var_declaration(self, name: Value) -> Completion:
        return NormalCompletion(value(name in self.var_names))

    def has_lexical_declaration(self, name: Value) -> Completion:
        return self.declarative_record.has_binding(name)

    def has_restricted_global_property(self, name: Value) -> Completion:
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-hasrestrictedglobalproperty

    def can_declare_global_var(self, name: Value) -> Completion:
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-candeclareglobalvar

    def can_declare_global_function(self, name: Value) -> Completion:
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-candeclareglobalfunction

    def create_global_var_binding(self, name: Value,
                                  deletable: Value) -> Completion:
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-createglobalvarbinding

    def create_global_function_binding(self, name: Value, val: Value,
                                       deletable: Value) -> Completion:
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-createglobalfunctionbinding
