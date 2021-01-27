import pandas as pd

from pandas_addons.register import DEFAULT_PANDAS_OBJECTS, register


@register(*DEFAULT_PANDAS_OBJECTS)
def concat(pandas_object, *args, **kwargs):
    objs, *other_args = args
    objs = [obj(pandas_object) if callable(obj) else obj for obj in objs]
    return pd.concat([pandas_object, *objs], *other_args, **kwargs)
