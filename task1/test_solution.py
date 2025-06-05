import unittest

from solution import strict


class TestStrictDecorator(unittest.TestCase):


    def test_int_and_str_success(self):
        @strict
        def f(x: int, y:str):
            return x ,y
        self.assertEqual(f(1,'a'), (1,'a'))

    def test_int_and_str_failure(self):
        @strict
        def f(x: int, y: str):
            return x, y
        with self.assertRaises(TypeError):
            f('1', 'a')

    def test_float_and_bool_success(self):
        @strict
        def f(x: float, y: bool):
            return x, y
        self.assertEqual(f(5.0, True), (5.0, True))

    def test_float_and_bool_failure(self):
        @strict
        def f(x: float, y: bool):
            return x, y
        with self.assertRaises(TypeError):
            f(2.0, 1.0)

    def test_multiple_arguments_success(self):
        @strict
        def f(a: int, b: str, c: float, d: bool):
            return (a, b, c, d)
        self.assertEqual(f(1, "a", 2.0, True), (1, "a", 2.0, True))

    def test_multiple_arguments_failure(self):
        @strict
        def f(a: int, b: str, c: float, d: bool):
            return (a, b, c, d)
        with self.assertRaises(TypeError):
            f(1, "a", "b", True)

    def test_keyword_arguments_success(self):
        @strict
        def f(x: int, y: str):
            return f"{x} {y}"
        self.assertEqual(f(x=1, y="a"), "1 a")

    def test_keyword_arguments_failure(self):
        @strict
        def f(x: int, y: str):
            return f"{x} {y}"
        with self.assertRaises(TypeError):
            f(x=1, y=2)