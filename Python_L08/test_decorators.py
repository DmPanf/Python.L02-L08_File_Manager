import unittest
import time
from io import StringIO
from contextlib import redirect_stdout

from decorators import check_time, add_separators


class TestDecorators(unittest.TestCase):

    def test_check_time_decorator(self):

        @check_time
        def my_func():
            time.sleep(0.5)

        with redirect_stdout(StringIO()) as f:
            my_func()
            expected_output = '[*] Время выполнения: '
            self.assertTrue(expected_output in f.getvalue())

    def test_add_separators_decorator(self):

        @add_separators
        def my_func():
            return 1

        with redirect_stdout(StringIO()) as f:
            my_func()
            expected_output = '-' * 35
            self.assertTrue(expected_output in f.getvalue())


if __name__ == '__main__':
    unittest.main()
