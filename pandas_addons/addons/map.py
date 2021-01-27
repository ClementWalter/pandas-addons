import os
from multiprocessing import Pool

import pandas as pd
from tqdm import tqdm

from pandas_addons.register import register


# noinspection PyShadowingBuiltins
@register(pd.Series)
def map(input_series, arg, **kwargs):
    if not kwargs.get("parallel"):
        if "parallel" in kwargs:
            del kwargs["parallel"]
        return input_series.map(arg, **kwargs)
    return pd.Series(
        list(
            tqdm(
                Pool(kwargs.get("processes", os.cpu_count())).imap(arg, input_series.tolist()),
                total=len(input_series),
            )
        ),
        name=input_series.name,
        index=input_series.index,
    )
