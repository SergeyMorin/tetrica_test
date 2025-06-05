import unittest
from solution import appearance, tests

class TestAppearance(unittest.TestCase):
    def test_cases(self):

        for i, test in enumerate(tests):
            with self.subTest(i=i):
                self.assertEqual(appearance(test['intervals']), test['answer'])

if __name__ == '__main__':
    unittest.main()
