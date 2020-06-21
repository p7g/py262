from typing import Any, Union

from py262.environment import LexicalEnvironment
from py262.module_record import ModuleRecord
from py262.realm import RealmRecord
from py262.value import Value

ScriptOrModule = Union[ModuleRecord, None]  # TODO: ScriptRecord


class ExecutionContext:
    code_evaluation_state: Any
    function: Value
    realm: RealmRecord
    script_or_module: ScriptOrModule
    lexical_environment: LexicalEnvironment
    variable_environment: LexicalEnvironment


class GeneratorExecutionContext(ExecutionContext):
    generator: Value
