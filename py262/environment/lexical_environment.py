from typing import TYPE_CHECKING, Union

from .abstract_environment import AbstractEnvironment

if TYPE_CHECKING:
    from py262.value import Value  # noqa: W0611


class LexicalEnvironment:
    environment_record: AbstractEnvironment
    outer_lexical_environment: Union['Value', 'LexicalEnvironment']
