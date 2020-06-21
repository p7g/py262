from py262.environment import DeclarativeEnvironmentRecord
from py262.value import Value
from tests.testutils import TestCase


class TestDeclarativeEnvironment(TestCase):
    def setUp(self):
        self.env = DeclarativeEnvironmentRecord()

    def test_has_binding(self):
        self.assertNormalCompletion(
            self.env.create_mutable_binding('test', Value.false))
        value = self.assertNormalCompletion(self.env.has_binding('test'))
        self.assertIs(value, Value.true)

    def test_create_mutable_binding(self):
        self.assertNormalCompletion(
            self.env.create_mutable_binding('testBinding', Value.false))
        self.assertNormalCompletion(
            self.env.initialize_binding('testBinding', Value.null))
        self.assertNormalCompletion(
            self.env.set_mutable_binding('testBinding', Value.true,
                                         Value.true))
        value = self.assertNormalCompletion(
            self.env.get_binding_value('testBinding', Value.false))
        self.assertIs(value, Value.true)

    def test_create_immutable_binding(self):
        self.assertNormalCompletion(
            self.env.create_immutable_binding('testBinding', Value.true))
        self.assertNormalCompletion(
            self.env.initialize_binding('testBinding', Value.false))
        value = self.assertNormalCompletion(
            self.env.get_binding_value('testBinding', Value.false))
        self.assertIs(value, Value.false)
        self.assertThrowCompletion(  # TODO assert value is TypeError
            self.env.set_mutable_binding('testBinding', Value.true,
                                         Value.false))

    def test_initialize_binding(self):
        pass

    def test_set_mutable_binding(self):
        # non-existant binding
        #   strict and not strict
        # uninitialized binding
        #   on strict and not strict bindings
        # immutable binding
        #   strict and not strict bindings
        pass

    def test_get_binding_value(self):
        # get value
        # uninitialized binding always ReferenceError
        pass

    def test_delete_binding(self):
        # true if deleted, false if not deletable
        pass

    def test_has_super_binding(self):
        self.assertIs(
            Value.false,
            self.assertNormalCompletion(self.env.has_super_binding()))

    def test_with_base_object(self):
        self.assertIs(Value.undefined,
                      self.assertNormalCompletion(self.env.with_base_object()))
