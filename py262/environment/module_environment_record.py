from dataclasses import dataclass
from typing import Dict

from py262.completion import Completion, NormalCompletion, ThrowCompletion
from py262.module_record import ModuleRecord
from py262.value import Value, value

from .declarative_environment_record import DeclarativeEnvironmentRecord


@dataclass
class IndirectBinding:
    module_record: ModuleRecord
    name2: Value


class ModuleEnvironmentRecord(DeclarativeEnvironmentRecord):
    indirect_bindings: Dict[Value, IndirectBinding]  # noqa

    def __init__(self):
        super().__init__()
        self.indirect_bindings = {}

    def get_binding_value(self, name: Value, strict: Value) -> Completion:
        assert strict is Value.true
        assert name in self.bindings or name in self.indirect_bindings
        if name in self.indirect_bindings:
            binding = self.indirect_bindings[name]
            m = binding.module_record
            n2 = binding.name2
            target_env = m.environment
            if target_env is None:
                return ThrowCompletion(value('new ReferenceError'))  # FIXME
            target_er = target_env.environment_record
            return target_er.get_binding_value(n2, Value.true)
        binding2 = self.bindings[name]
        if not binding2.initialized:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        return NormalCompletion(binding2.value)

    def delete_binding(self, name: Value) -> Completion:
        assert False, 'This method should never be invoked'

    def has_this_binding(self) -> Value:
        return Value.true

    def get_this_binding(self) -> Completion:
        return NormalCompletion(Value.undefined)

    def create_import_binding(self, name: Value, m: ModuleRecord,
                              name2: Value) -> Completion:
        assert name not in self.bindings and name not in self.indirect_bindings
        assert isinstance(m, ModuleRecord)
        # assert m.environment.has_binding(name)  FIXME: only when m.environment
        # is instantiated?
        self.indirect_bindings[name] = IndirectBinding(module_record=m,
                                                       name2=name2)
        return NormalCompletion(None)
