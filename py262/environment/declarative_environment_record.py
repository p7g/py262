from dataclasses import dataclass
from typing import Dict, Optional

from py262.completion import Completion, NormalCompletion, ThrowCompletion
from py262.value import Value, value

from .abstract_environment_record import AbstractEnvironmentRecord


@dataclass
class Binding:
    initialized: bool
    mutable: bool
    deletable: bool
    strict: bool
    value: Optional[Value] = None


class DeclarativeEnvironmentRecord(AbstractEnvironmentRecord):
    bindings: Dict[Value, Binding]

    def __init__(self):
        self.bindings = {}

    def has_binding(self, name: Value) -> Completion:
        return NormalCompletion(value(name in self.bindings))

    def create_mutable_binding(self, name: Value,
                               deletable: Value) -> Completion:
        assert name not in self.bindings
        self.bindings[name] = Binding(
            initialized=False,
            mutable=True,
            deletable=deletable is Value.true,
            strict=False,
        )
        return NormalCompletion(None)

    def create_immutable_binding(self, name: Value,
                                 strict: Value) -> Completion:
        self.bindings[name] = Binding(
            initialized=False,
            mutable=False,
            strict=strict is Value.true,
            deletable=False,
        )
        return NormalCompletion(None)

    def initialize_binding(self, name: Value, val: Value) -> Completion:
        assert name in self.bindings and not self.bindings[name].initialized
        binding = self.bindings[name]
        binding.value = val
        binding.initialized = True
        return NormalCompletion(None)

    def set_mutable_binding(self, name: Value, val: Value,
                            strict: Value) -> Completion:
        if name not in self.bindings:
            if strict == Value.true:
                return ThrowCompletion(value('new TypeError'))  # FIXME
            self.create_mutable_binding(name, Value.true)
            self.initialize_binding(name, val)
            return NormalCompletion(None)
        if self.bindings[name].strict:
            strict = Value.true
        if not self.bindings[name].initialized:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        if self.bindings[name].mutable:
            self.bindings[name].value = val
        else:
            assert 'trying to change value of immutable binding'
            if strict is Value.true:
                return ThrowCompletion(value('new TypeError'))  # FIXME
        return NormalCompletion(None)

    def get_binding_value(self, name: Value, _s: Value) -> Completion:
        assert name in self.bindings
        if not self.bindings[name].initialized:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        return NormalCompletion(self.bindings[name].value)

    def delete_binding(self, name: Value) -> Completion:
        assert name in self.bindings
        if not self.bindings[name].deletable:
            return NormalCompletion(Value.false)
        del self.bindings[name]
        return NormalCompletion(Value.true)

    def has_this_binding(self) -> Completion:
        return NormalCompletion(Value.false)

    def has_super_binding(self) -> Completion:
        return NormalCompletion(Value.false)

    def with_base_object(self) -> Completion:
        return NormalCompletion(Value.undefined)
