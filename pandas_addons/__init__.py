from functools import partial

import pandas as pd

from pandas_addons import addons
from pandas_addons.register import ACCESSORS, DEFAULT_PANDAS_OBJECTS, register


def init():
    for accessor_name, pandas_objects_mapping in ACCESSORS.items():
        for pdo, accessor_ in pandas_objects_mapping.items():
            setattr(pdo, accessor_name, accessor_)


@pd.api.extensions.register_dataframe_accessor("pda")
@pd.api.extensions.register_series_accessor("pda")
@pd.api.extensions.register_index_accessor("pda")
class PandasAddons:
    def __init__(self, pandas_object):
        self._pandas_object = pandas_object

    def __getattr__(self, item):
        accessor = ACCESSORS[item].get(self._pandas_object.__class__)
        if accessor is None:
            raise ValueError(
                f"Accessor {item} is not defined for objects of type {self._pandas_object.__class__.__name__}"
            )
        return partial(accessor, self._pandas_object)


__all__ = ["init", "register"]
