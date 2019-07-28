from typing import Union

from py262.completion import Completion, NormalCompletion
from py262.reference import Reference
from py262.value import Value, type_of

from .declarative_environment import DeclarativeEnvironment
from .function_environment import FunctionEnvironment
from .global_environment import GlobalEnvironment
from .lexical_environment import LexicalEnvironment
from .object_environment import ObjectEnvironment


def get_identifier_reference(lex: Union[Value, LexicalEnvironment],
                             name: Value, strict: Value) -> Completion:
    if lex is Value.null:
        return NormalCompletion(
            Reference(base=Value.undefined,
                      referenced_name=name,
                      is_strict=strict))
    assert isinstance(
        lex, LexicalEnvironment)  # FIXME: is this assumption accurate?
    exists_completion = lex.environment_record.has_binding(name)
    if exists_completion.is_abrupt():
        return exists_completion
    exists = exists_completion.value
    if exists is Value.true:
        return NormalCompletion(
            Reference(base=lex.environment_record,
                      referenced_name=name,
                      is_strict=strict))
    return get_identifier_reference(lex.outer_lexical_environment, name,
                                    strict)


def new_declarative_environment(outer_env: LexicalEnvironment
                                ) -> LexicalEnvironment:
    env = LexicalEnvironment()
    env_rec = DeclarativeEnvironment()
    env.environment_record = env_rec
    env.outer_lexical_environment = outer_env
    return env


def new_object_environment(obj: Value, outer_env: LexicalEnvironment
                           ) -> LexicalEnvironment:
    env = LexicalEnvironment()
    env_rec = ObjectEnvironment()
    env_rec.binding_object = obj
    env.environment_record = env_rec
    env.outer_lexical_environment = outer_env
    return env


def new_function_environment(fn: Value,
                             new_target: Value) -> LexicalEnvironment:
    assert type_of(fn) == 'function'
    assert type_of(new_target) in ('undefined', 'object')
    env = LexicalEnvironment()
    env_rec = FunctionEnvironment()
    env_rec.function_object = fn
    # https://tc39.es/ecma262/#sec-newfunctionenvironment
    raise NotImplementedError()
    return env


def new_global_environmetn(g: Value, this_value: Value) -> LexicalEnvironment:
    env = LexicalEnvironment()
    obj_rec = ObjectEnvironment()
    obj_rec.binding_object = g
    decl_rec = DeclarativeEnvironment()
    global_rec = GlobalEnvironment()
    global_rec.object_record = obj_rec
    global_rec.global_this_value = this_value
    global_rec.declarative_record = decl_rec
    global_rec.var_names = []
    env.environment_record = global_rec
    env.outer_lexical_environment = Value.null
    return env


def new_module_environment(env: LexicalEnvironment) -> LexicalEnvironment:
    # https://tc39.es/ecma262/#sec-newmoduleenvironment
    raise NotImplementedError()
