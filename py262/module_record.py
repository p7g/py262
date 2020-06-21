from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

from py262.environment import LexicalEnvironment
from py262.realm import RealmRecord
from py262.value import Value


@dataclass
class ResolvedBinding:
    module: 'ModuleRecord'
    binding_name: Value


class ModuleRecord(ABC):
    realm: Optional[RealmRecord]
    environment: Optional[LexicalEnvironment]
    namespace: Value
    host_defined: Any

    @abstractmethod
    def get_exported_names(self, export_star_set=None):
        pass

    @abstractmethod
    def resolve_export(self, export_name: Value,
                       resolved_set=None) -> ResolvedBinding:
        pass

    @abstractmethod
    def link(self):
        pass

    @abstractmethod
    def evaluate(self) -> Value:
        pass
