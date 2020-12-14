# Welcome to Pandas add-ons

Pandas-addons, or simply pda, aims at providing new methods to be used directly onto pandas object in a natural (chained)
manner.

While the [official pandas documentation](https://pandas.pydata.org/pandas-docs/stable/development/extending.html) do 
explain how to write custom accessors to pandas object, the [pandas ecosystem](https://pandas.pydata.org/pandas-docs/stable/ecosystem.html#ecosystem)
still lacks a unified entrypoint for doing more with pandas.

Especially these above-mentioned libraries try to tackle a single problem on their own leveraging the usual core
pandas library. On the opposite, this repo strives to make the new accessors as natual as possible so that using
base pandas or pandas-addons accessors should look the same. It is really about adding features to pandas, not 
building another library relying on pandas.

## Usage

In this spirit, there is two way to use the accessors defined in this package after importing it:

- by calling the `pda` accessor directly on a `pd.Series`, `pd.DataFrame` or `pd.Index` object

```python
import pandas as pd
import pandas_addons as pda

pd.DataFrame([]).pda.assert_(lambda df: df.empty)
```

- or by calling the `init` method so that the accessors are added to pandas objects and are directly accessible from them:

```python
import pandas as pd
import pandas_addons as pda

pda.init()

(
    pd.DataFrame({"a": [1, 2]})
    .assert_(lambda df: (df.a > 0).all())
    .assign(b=lambda df: 1 / df.a)
)
```

## Extending pandas-addons

It is also possible to add new accessors on-the-fly on any type of pandas object simply by calling the `register`
decorator:

```python
import pandas as pd
import pandas_addons as pda

@pda.register(pd.Timedelta)
def custom_timedelta_accessor(df, *args, **kwargs):
    print(args)
    print(kwargs)

pda.init()
pd.Timedelta(0).custom_timedelta_accessor("It is cool!", check_my_kwarg="swag")
# ('It is cool!',)
# {'check_my_kwarg': 'swag'}
```
