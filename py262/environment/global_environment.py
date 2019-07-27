from typing import List

from py262.completion import Completion, NormalCompletion, ThrowCompletion
from py262.value import Value, value

from .declarative_environment import DeclarativeEnvironment
from .object_environment import ObjectEnvironment


class GlobalEnvironment:
    object_record: ObjectEnvironment
    global_this_value: Value
    declarative_record: DeclarativeEnvironment
    var_names: List[str]

    def has_binding(self, name) -> Completion:
        if self.declarative_record.has_binding(name).value is Value.true:
            return NormalCompletion(Value.true)
        completion = self.object_record.has_binding(name)
        if completion.is_abrupt():
            return completion
        return NormalCompletion(completion.value)

    def create_mutable_binding(self, name, deletable: Value) -> Completion:
        if self.declarative_record.has_binding(name).value is Value.true:
            return ThrowCompletion(value('new TypeError'))  # FIXME
        return self.declarative_record.create_mutable_binding(name, deletable)
