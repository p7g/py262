import unittest

from py262.utils.schrodinger_property import schrodinger_property


class SchrodingerClass:
    def __init__(self):
        self.__some_prop = 0

    @schrodinger_property
    def some_prop(self):
        return self.__some_prop

    @some_prop.setter
    def some_prop(self, value):  # pylint: disable=function-redefined
        self.__some_prop = value


class TestSchrodingerProperty(unittest.TestCase):
    def test_setting_value(self):
        instance = SchrodingerClass()

        instance.some_prop = 123
        instance.some_prop = 234
        instance.some_prop = 345

    def test_getting_value(self):
        instance = SchrodingerClass()

        instance.some_prop = 123

        self.assertEqual(instance.some_prop, 123)

    def test_setting_after_get(self):
        instance = SchrodingerClass()
        instance.some_prop = 848

        self.assertEqual(instance.some_prop, 848)

        with self.assertRaises(AssertionError):
            instance.some_prop = 344

    def test_multiple_properties(self):
        class A:
            @schrodinger_property
            def prop_a(self):
                return self.__a

            @prop_a.setter
            def prop_a(self, value):  # pylint: disable=function-redefined
                self.__a = value

            @schrodinger_property
            def prop_b(self):
                return self.__b

            @prop_b.setter
            def prop_b(self, value):  # pylint: disable=function-redefined
                self.__b = value

        a = A()

        a.prop_a = 123
        a.prop_b = a.prop_a + 123

        a.prop_b = 50
