from py262.completion import Completion
from py262.value import Value

from .lexical_environment import LexicalEnvironment


def get_identifier_reference(lex: LexicalEnvironment, name: Value,
                             strict: Value) -> Completion:
    if lex is Value.null:
        pass
    raise NotImplementedError()
