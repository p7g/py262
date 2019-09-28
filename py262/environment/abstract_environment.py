from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from py262.completion import Completion
    from py262.value import Value


class AbstractEnvironment(ABC):
    @abstractmethod
    def has_binding(self, name) -> 'Completion':
        pass

    @abstractmethod
    def create_mutable_binding(self, name, deletable: 'Value') -> 'Completion':
        pass

    @abstractmethod
    def create_immutable_binding(self, name, strict: 'Value') -> 'Completion':
        pass

    @abstractmethod
    def initialize_binding(self, name, value: 'Value') -> 'Completion':
        pass

    @abstractmethod
    def set_mutable_binding(self, name, value: 'Value',
                            strict: 'Value') -> 'Completion':
        pass

    @abstractmethod
    def get_binding_value(self, name, strict: 'Value') -> 'Completion':
        pass

    @abstractmethod
    def delete_binding(self, name) -> 'Completion':
        pass

    @abstractmethod
    def has_this_binding(self) -> 'Completion':
        pass

    @abstractmethod
    def has_super_binding(self) -> 'Completion':
        pass

    @abstractmethod
    def with_base_object(self) -> 'Completion':
        pass
