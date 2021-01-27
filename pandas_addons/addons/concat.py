import pandas as pd

from pandas_addons.register import DEFAULT_PANDAS_OBJECTS, register


@register(*DEFAULT_PANDAS_OBJECTS)
def concat(pandas_object, *args, **kwargs):
    objs, *other_args = args
    return pd.concat([pandas_object, *objs], *other_args, **kwargs)
