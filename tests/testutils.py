import unittest

from py262.completion import Completion, CompletionType


class TestCase(unittest.TestCase):
    def assertNormalCompletion(self, completion: Completion):
        self.assertFalse(completion.is_abrupt())
        return completion.value

    def assertAbruptCompletion(self, completion: Completion):
        self.assertTrue(completion.is_abrupt())
        return completion.value

    def assertThrowCompletion(self, completion: Completion):
        self.assertEqual(completion.type, CompletionType.THROW)
