import unittest
from utils import call_rbo


class TestRBO(unittest.TestCase):
    def test_instatiate_rbo_class(self):
        subject_rbo = RBO()
        self.assertIsInstance(subject_rbo, RBO)

    def test_rbo_call_without_arguments(self):
        subject_rbo = RBO()
        result = subject_rbo.call()
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
