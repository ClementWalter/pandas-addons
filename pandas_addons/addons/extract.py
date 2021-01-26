import pandas as pd

from pandas_addons.register import register


@register(pd.DataFrame)
def extract(input_dataframe, column_name, *args, **kwargs):
    if column_name not in input_dataframe:
        raise ValueError(f"{column_name} not found in {input_dataframe}")

    args = [*args]
    if len(args) == 3:
        args[2] = True
        kwargs = {}
    else:
        kwargs["expand"] = True

    return pd.concat(
        [
            input_dataframe,
            input_dataframe[column_name].str.extract(*args, **kwargs),
        ],
        axis=1,
    )
