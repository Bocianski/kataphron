import unittest

# FIXME: This is just an example, don't include it in the project
class ExampleTest(unittest.TestCase):
    def test_example(self):
        #! given
        string = "test"

        #! when
        stringLower = string.upper()

        #! then
        self.assertEqual(stringLower, "TEST")
        self.assertNotEqual(stringLower, string)