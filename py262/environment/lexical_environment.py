from typing import Optional

from .abstract_environment_record import AbstractEnvironmentRecord


class LexicalEnvironment:
    environment_record: AbstractEnvironmentRecord
    outer_lexical_environment: Optional['LexicalEnvironment']
