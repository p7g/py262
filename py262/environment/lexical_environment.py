from typing import Union

from py262.value import Value

from .abstract_environment import AbstractEnvironment


class LexicalEnvironment:
    environment_record: AbstractEnvironment
    outer_lexical_environment: Union[Value, 'LexicalEnvironment']
