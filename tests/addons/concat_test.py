from unittest.mock import patch, sentinel

import pandas as pd
import pytest

from pandas_addons.addons.concat import concat
from pandas_addons.register import DEFAULT_PANDAS_OBJECTS


@pytest.mark.parametrize("pandas_object", DEFAULT_PANDAS_OBJECTS)
@patch.object(pd, "concat")
class TestConcat:
    def test_should_call_concat_with_given_args_and_kwargs(self, mock_concat, pandas_object):
        concat(pandas_object, [], sentinel.args, kwarg=sentinel.kwarg)
        mock_concat.assert_called_once_with([pandas_object], sentinel.args, kwarg=sentinel.kwarg)

    def test_should_call_callable_arg_with_pandas_object(self, mock_concat, pandas_object):
        concat(pandas_object, [lambda x: "callable"])
        mock_concat.assert_called_once_with([pandas_object, "callable"])
