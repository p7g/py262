from py262.value import (UNDEFINED, BooleanValue, NullValue, ObjectValue,
                         UndefinedValue, Value, value)
from tests.testutils import TestCase


class TestValue(TestCase):
    def test_true(self):
        self.assertIsInstance(Value.true, BooleanValue)
        self.assertIs(Value.true, Value.true)
        self.assertIs(Value.true.inner_value, True)

    def test_false(self):
        self.assertIsInstance(Value.false, BooleanValue)
        self.assertIs(Value.false, Value.false)
        self.assertIs(Value.false.inner_value, False)

    def test_null(self):
        self.assertIsInstance(Value.null, NullValue)
        self.assertIs(Value.null, Value.null)

    def test_undefined(self):
        self.assertIsInstance(Value.undefined, UndefinedValue)
        self.assertIs(Value.undefined, Value.undefined)

    def test_is_primitive(self):
        self.assertTrue(Value.is_primitive(Value.true))
        self.assertTrue(Value.is_primitive(Value.false))
        self.assertTrue(Value.is_primitive(Value.null))
        self.assertTrue(Value.is_primitive(Value.undefined))
        self.assertFalse(Value.is_primitive(ObjectValue()))

    def test_value(self):
        self.assertIs(value(True), Value.true)
        self.assertIs(value(False), Value.false)
        self.assertIs(value(None), Value.null)
        self.assertIs(value(UNDEFINED), Value.undefined)
        self.assertIs(value(), Value.undefined)
