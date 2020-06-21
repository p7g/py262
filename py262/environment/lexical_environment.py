from typing import Optional

from .environment_record import EnvironmentRecord


class LexicalEnvironment:
    environment_record: EnvironmentRecord
    outer_lexical_environment: Optional['LexicalEnvironment']
