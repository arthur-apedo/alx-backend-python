#!/usr/bin/env python3
"""
    Duck-typed annotations for safely_get_vavlue function
"""
from typing import MutableMapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: MutableMapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        Returns the value for the given key if it exists, otherwise
        return the default
    """
    if key in dct:
        return dct[key]
    else:
        return default
