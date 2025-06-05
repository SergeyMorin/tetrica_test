import unittest

from solution import wiki_animal_counter, fetch_from_local, START_DIR


class TestWikiAnimalCounter(unittest.TestCase):


    def test_local_pages(self):
        expected = {
            'А': 300,
            'Б': 180,
            'В': 120,
        }
        result = wiki_animal_counter(START_DIR, {}, fetch_from_local)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
