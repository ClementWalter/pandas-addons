from unittest.mock import patch, sentinel

import pandas as pd
import pytest

from pandas_addons.addons.concat import concat
from pandas_addons.register import DEFAULT_PANDAS_OBJECTS


class TestConcat:
    @pytest.mark.parametrize("pandas_object", DEFAULT_PANDAS_OBJECTS)
    @patch.object(pd, "concat")
    def test_should_call_concat_with_given_args_and_kwargs(self, mock_concat, pandas_object):
        concat(pandas_object, [], sentinel.args, kwarg=sentinel.kwarg)
        mock_concat.assert_called_once_with([pandas_object], sentinel.args, kwarg=sentinel.kwarg)
