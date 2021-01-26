from unittest.mock import patch, sentinel

import pandas as pd
import pytest

from pandas_addons.addons.extract import extract


class TestExtract:
    def test_should_raise_value_error_when_column_is_not_fount(self):
        with pytest.raises(ValueError) as error:
            extract(pd.DataFrame(), "column_name")
        assert str(error.value) == f"column_name not found in {pd.DataFrame()}"

    @patch.object(pd.Series.str, "extract", return_value=pd.DataFrame(columns=["other_column"]))
    def test_should_call_extract_on_series_with_given_kwargs(self, mock_extract):
        input_dataframe = pd.DataFrame(columns=["column_name"])
        extract(input_dataframe, "column_name", sentinel.args, kwarg=sentinel.kwarg)
        mock_extract.assert_called_once_with(sentinel.args, kwarg=sentinel.kwarg)

    @patch.object(pd.Series.str, "extract", return_value=pd.DataFrame(columns=["other_column"]))
    def test_should_enforce_expand_given_as_arg(self, mock_extract):
        input_dataframe = pd.DataFrame(columns=["column_name"])
        extract(input_dataframe, "column_name", sentinel.arg_0, sentinel.arg_1, sentinel.arg_2)
        mock_extract.assert_called_once_with(sentinel.arg_0, sentinel.arg_1, True)

    @patch.object(pd.Series.str, "extract", return_value=pd.DataFrame(columns=["other_column"]))
    def test_should_enforce_expand_given_as_kwarg(self, mock_extract):
        input_dataframe = pd.DataFrame(columns=["column_name"])
        extract(input_dataframe, "column_name", sentinel.args, expand=sentinel.expand)
        mock_extract.assert_called_once_with(sentinel.args, expand=True)

    def test_should_extract_and_assign_series(self):
        input_dataframe = pd.DataFrame({"filepath": ["path/to/file_0", "path/to/file_1"]})
        output_dataframe = extract(
            input_dataframe,
            "filepath",
            r"^(?P<basename>.*)\/(?P<filename>\w+)_(?P<version>\d+)$",
        )
        pd.testing.assert_frame_equal(
            output_dataframe,
            input_dataframe.assign(
                basename=["path/to", "path/to"],
                filename=["file", "file"],
                version=["0", "1"],
            ),
        )
