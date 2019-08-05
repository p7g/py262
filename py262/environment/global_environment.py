from typing import List

from py262.completion import NormalCompletion, ThrowCompletion
from py262.value import Value, value

from .abstract_environment import AbstractEnvironment
from .declarative_environment import DeclarativeEnvironment
from .object_environment import ObjectEnvironment


class GlobalEnvironment(AbstractEnvironment):
    object_record: ObjectEnvironment
    global_this_value: Value
    declarative_record: DeclarativeEnvironment
    var_names: List[str]

    def has_binding(self, name):
        if self.declarative_record.has_binding(name).value is Value.true:
            return NormalCompletion(Value.true)
        return self.object_record.has_binding(name)

    def create_mutable_binding(self, name, deletable):
        if self.declarative_record.has_binding(name).value is Value.true:
            return ThrowCompletion(value('new TypeError'))  # FIXME
        return self.declarative_record.create_mutable_binding(name, deletable)

    def create_immutable_binding(self, name, strict):
        if self.declarative_record.has_binding(name) is Value.true:
            return ThrowCompletion(value('new TypeError'))  # FIXME
        return self.declarative_record.create_immutable_binding(name, strict)

    def initialize_binding(self, name, val):
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.initialize_binding(name, val)
        assert 'binding must be in object environment if it exists'
        return self.object_record.initialize_binding(name, val)

    def set_mutable_binding(self, name, val, strict):
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.set_mutable_binding(
                name, val, strict)
        return self.object_record.set_mutable_binding(name, val, strict)

    def get_binding_value(self, name, strict):
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.get_binding_value(name, strict)
        return self.object_record.get_binding_value(name, strict)

    # https://tc39.es/ecma262/#sec-global-environment-records-deletebinding-n
    def delete_binding(self, name):
        if self.declarative_record.has_binding(name) is Value.true:
            return self.declarative_record.delete_binding(name)
        raise NotImplementedError()

    def has_this_binding(self):
        return NormalCompletion(Value.true)

    def has_super_binding(self):
        return NormalCompletion(Value.false)

    def with_base_object(self):
        return NormalCompletion(Value.undefined)

    def get_this_binding(self):
        return NormalCompletion(self.global_this_value)

    def has_var_declaration(self, name):
        return NormalCompletion(value(name in self.var_names))

    def has_lexical_declaration(self, name):
        return self.declarative_record.has_binding(name)

    def has_restricted_global_property(self, name):
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-hasrestrictedglobalproperty

    def can_declare_global_var(self, name):
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-candeclareglobalvar

    def can_declare_global_function(self, name):
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-candeclareglobalfunction

    def create_global_var_binding(self, name, deletable):
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-createglobalvarbinding

    def create_global_function_binding(self, name, val, deletable):
        raise NotImplementedError(
        )  # https://tc39.es/ecma262/#sec-createglobalfunctionbinding
