from py262.completion import NormalCompletion, ThrowCompletion
from py262.value import Value, value

from .abstract_environment import AbstractEnvironment


class DeclarativeEnvironment(AbstractEnvironment):
    def __init__(self):
        self.bindings = {}

    def has_binding(self, name):
        return NormalCompletion(value(name in self.bindings))

    def create_mutable_binding(self, name, deletable):
        assert name not in self.bindings
        self.bindings[name] = {
            'initialized': False,
            'mutable': True,
            'deletable': deletable is Value.true,
            'strict': False,
        }
        return NormalCompletion(None)

    def create_immutable_binding(self, name, strict):
        self.bindings[name] = {
            'initialized': False,
            'mutable': False,
            'strict': strict is Value.true,
            'deletable': False,
        }
        return NormalCompletion(None)

    def initialize_binding(self, name, val):
        assert name in self.bindings and not self.bindings[name]['initialized']
        binding = self.bindings[name]
        binding['value'] = val
        binding['initialized'] = True
        return NormalCompletion(None)

    def set_mutable_binding(self, name, val, strict):
        if name not in self.bindings:
            if strict == Value.true:
                return ThrowCompletion(value('new TypeError'))  # FIXME
            self.create_mutable_binding(name, Value.true)
            self.initialize_binding(name, val)
            return NormalCompletion(None)
        if self.bindings[name]['strict']:
            strict = Value.true
        if not self.bindings[name]['initialized']:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        if self.bindings[name]['mutable']:
            self.bindings[name]['value'] = val
        else:
            assert 'trying to change value of immutable binding'
            if strict is Value.true:
                return ThrowCompletion(value('new TypeError'))  # FIXME
        return NormalCompletion(None)

    def get_binding_value(self, name, _s):
        assert name in self.bindings
        if not self.bindings[name]['initialized']:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        return NormalCompletion(self.bindings[name]['value'])

    def delete_binding(self, name):
        assert name in self.bindings
        if not self.bindings[name]['deletable']:
            return NormalCompletion(Value.false)
        del self.bindings[name]
        return NormalCompletion(Value.true)

    def has_this_binding(self):
        return NormalCompletion(Value.false)

    def has_super_binding(self):
        return NormalCompletion(Value.false)

    def with_base_object(self):
        return NormalCompletion(Value.undefined)
