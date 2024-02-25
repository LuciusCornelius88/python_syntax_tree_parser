import sys
import unittest
from parameterized import parameterized
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.main import *
from testcases import *


class TestParser(unittest.TestCase):

    def setUp(self) -> None:
        self.error = ParseException
        self.method = parse_subtree

    @parameterized.expand(parser_correct_cases)
    def test_parser_correct(self, input_case, expected_case):
        output = self.method(input_case)
        self.assertEqual(output, expected_case)

    @parameterized.expand(parser_raise_parse_exception_cases)
    def test_parser_raises(self, input_case):
        with self.assertRaises(self.error):
            self.method(input_case)


class TestNPExtractor(unittest.TestCase):

    def setUp(self) -> None:
        self.error = AttributeError
        self.method = extract_NP_subtrees

    @parameterized.expand(extractor_correct_cases)
    def test_extractor_correct(self, input_case, expected_case):
        output = self.method(input_case)
        self.assertEqual(output, expected_case)

    @parameterized.expand(extractor_raise_attr_error_cases)
    def test_extractor_raises(self, input_case):
        with self.assertRaises(self.error):
            self.method(input_case)


class TestCombinationsProcessing(unittest.TestCase):

    def setUp(self) -> None:
        self.error = TypeError
        self.create_combinations_method = create_combinations
        self.unite_combinations_method = unite_combinations
        self.normalize_original_method = normalize_original_list
        self.normalize_target_method = normalize_target_list

    @parameterized.expand(create_combinations_correct_cases)
    def test_create_combinations_correct(self, input_case, expected_case):
        output = self.create_combinations_method(input_case)
        self.assertEqual(output, expected_case)

    @parameterized.expand(create_combinations_raise_type_error_cases)
    def test_create_combinations_raises(self, input_case):
        with self.assertRaises(self.error):
            self.create_combinations_method(input_case)

    @parameterized.expand(unite_combinations_correct_cases)
    def test_unite_combinations_correct(self, input_case, expected_case):
        output = self.unite_combinations_method(input_case)
        self.assertEqual(output, expected_case)

    @parameterized.expand(unite_combinations_raise_type_error_cases)
    def test_unite_combinations_raises(self, input_case):
        with self.assertRaises(self.error):
            self.unite_combinations_method(input_case)

    @parameterized.expand(normalize_original_list_correct_cases)
    def test_normalize_original_list_correct(self, input_case, expected_case):
        output = self.normalize_original_method(input_case)
        self.assertEqual(output, expected_case)

    @parameterized.expand(normalize_original_list_raise_type_error_cases)
    def test_normalize_original_list_raises(self, input_case):
        with self.assertRaises(self.error):
            self.normalize_original_method(input_case)

    @parameterized.expand(normalize_target_list_correct_cases)
    def test_normalize_target_list_correct(self, input_case, expected_case):
        output = self.normalize_target_method(input_case)
        self.assertEqual(output, expected_case)

    @parameterized.expand(normalize_target_list_raise_type_error_cases)
    def test_normalize_target_list_raises(self, input_case):
        with self.assertRaises(self.error):
            self.normalize_target_method(input_case)


class TreesCreator(unittest.TestCase):
    def setUp(self) -> None:
        self.error = TypeError
        self.method = create_trees

    @parameterized.expand(trees_creator_correct_cases)
    def test_create_trees_correct(self, tree, original_positions, target_positions, limit, expected_case):
        output = self.method(tree, original_positions, target_positions, limit)
        self.assertEqual(output, expected_case)

    @parameterized.expand(trees_creator_raise_cases)
    def test_create_trees_raises(self, tree, original_positions, target_positions, limit):
        with self.assertRaises(self.error):
            self.method(tree, original_positions, target_positions, limit)


def main():
    try:
        test_suite_parser = unittest.TestLoader().loadTestsFromTestCase(TestParser)
        test_suite_extractor = unittest.TestLoader().loadTestsFromTestCase(TestNPExtractor)
        test_suite_comb_proc = unittest.TestLoader().loadTestsFromTestCase(TestCombinationsProcessing)
        test_suite_trees_creator = unittest.TestLoader().loadTestsFromTestCase(TreesCreator)

        unittest.TextTestRunner().run(test_suite_parser)
        unittest.TextTestRunner().run(test_suite_extractor)
        unittest.TextTestRunner().run(test_suite_comb_proc)
        unittest.TextTestRunner().run(test_suite_trees_creator)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
    delete_cache(Path(__file__).parent.parent)
