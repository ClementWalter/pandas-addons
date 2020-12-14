from collections import defaultdict

import pandas as pd

DEFAULT_PANDAS_OBJECTS = (pd.DataFrame, pd.Series, pd.Index)
ACCESSORS = defaultdict(dict)


def register(*args):
    pandas_objects = DEFAULT_PANDAS_OBJECTS if not args else args

    def decorator(fun):
        ACCESSORS[fun.__name__] = {pandas_object: fun for pandas_object in pandas_objects}
        return fun

    # handle @register call case
    if len(args) == 1 and args[0].__name__ not in dir(pd):
        decorated = args[0]
        pandas_objects = DEFAULT_PANDAS_OBJECTS
        return decorator(decorated)

    return decorator
