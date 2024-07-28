#!/usr/bin/env python3
"""
    Parametizing unittests with @parametized_expand
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """
       A class with test cases for requests to an Api
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, url, test_payload, mock_get_json):
        """ Tests output from a url """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get_json.return_value = mock_response
        result = get_json(url)
        self.assertIsInstance(result, dict)
        self.assertEqual(get_json(url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Tests the memoize decorator function """
    def test_memoize(self):
        """ Tests the memoize function """
        class TestClass:
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as mem:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mem.assert_called_once()
