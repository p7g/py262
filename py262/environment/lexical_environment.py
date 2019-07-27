from typing import Optional

from .abstract_environment import AbstractEnvironment


class LexicalEnvironment:
    environment_record: AbstractEnvironment
    outer_lexical_environment: Optional['LexicalEnvironment']
