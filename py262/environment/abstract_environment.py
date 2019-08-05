from abc import ABC, abstractmethod


class AbstractEnvironment(ABC):
    @abstractmethod
    def has_binding(self, name):
        pass

    @abstractmethod
    def create_mutable_binding(self, name, deletable):
        pass

    @abstractmethod
    def create_immutable_binding(self, name, strict):
        pass

    @abstractmethod
    def initialize_binding(self, name, value):
        pass

    @abstractmethod
    def set_mutable_binding(self, name, value, strict):
        pass

    @abstractmethod
    def get_binding_value(self, name, strict):
        pass

    @abstractmethod
    def delete_binding(self, name):
        pass

    @abstractmethod
    def has_this_binding(self):
        pass

    @abstractmethod
    def has_super_binding(self):
        pass

    @abstractmethod
    def with_base_object(self):
        pass
