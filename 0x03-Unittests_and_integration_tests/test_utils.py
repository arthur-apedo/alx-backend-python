#!/usr/bin/env python3
"""
    Parametizing unittests with @parametized_expand
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
        A class that defines methods to test a nested map
    """

    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """  Testing the nested map in parameterized with 3 diff inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ['a', 'b'])
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """  Testing the nested map errors raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
