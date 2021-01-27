from string import ascii_letters

import pandas as pd
import pytest


def fun(x):
    return x + 1


class TestMap:
    @pytest.mark.parametrize("parallel", (True, False))
    def test_should_return_same_value(self, parallel):
        s = pd.Series(range(4), index=list(ascii_letters[:4]))

        # noinspection PyUnresolvedReferences
        import pandas_addons as pda

        pd.testing.assert_series_equal(
            s.map(fun),
            s.pda.map(fun, parallel=parallel),
        )
