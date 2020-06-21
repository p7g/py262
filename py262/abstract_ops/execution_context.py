from typing import Optional

from py262.agent import surrounding_agent
from py262.completion import Completion
from py262.environment import (EnvironmentRecord, FunctionEnvironmentRecord,
                               GlobalEnvironmentRecord, LexicalEnvironment,
                               ModuleEnvironmentRecord)
from py262.execution_context import ScriptOrModule
from py262.reference import Reference
from py262.value import Value, value

from .lexical_environment import get_identifier_reference


def get_active_script_or_module() -> Optional[ScriptOrModule]:
    agent = surrounding_agent
    assert agent is not None
    for ctx in reversed(agent.execution_context_stack):
        if ctx.script_or_module is not None:
            return ctx.script_or_module
    return None


def resolve_binding(name: Value,
                    env: Optional[LexicalEnvironment] = None,
                    strict: bool = False) -> Reference:
    if not env:
        assert surrounding_agent is not None
        env = surrounding_agent.running_execution_context.lexical_environment
    assert isinstance(env, LexicalEnvironment)
    ref = get_identifier_reference(env, name, value(strict))
    assert isinstance(ref, Reference)
    return ref


def get_this_environment() -> EnvironmentRecord:
    assert surrounding_agent is not None
    lex = surrounding_agent.running_execution_context.lexical_environment
    while True:
        env_rec = lex.environment_record
        if env_rec.has_this_binding() is Value.true:
            return env_rec
        outer = lex.outer_lexical_environment
        assert outer is not None
        lex = outer


def resolve_this_binding() -> Completion:
    env_rec = get_this_environment()
    assert isinstance(env_rec,
                      (FunctionEnvironmentRecord, GlobalEnvironmentRecord,
                       ModuleEnvironmentRecord))
    return env_rec.get_this_binding()


def get_new_target() -> Value:
    env_rec = get_this_environment()
    assert isinstance(env_rec, FunctionEnvironmentRecord)
    return env_rec.new_target


def get_global_object() -> Value:
    assert surrounding_agent is not None
    current_realm = surrounding_agent.running_execution_context.realm
    return current_realm.global_object
