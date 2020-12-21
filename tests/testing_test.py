from unittest.mock import patch

import pandas as pd

from pandas_addons.testing import assert_pdo_equal


class TestAssertPdoEqual:
    @patch.object(pd.testing, "assert_frame_equal")
    def test_should_map_to_frame_equal(self, mock_frame_equal):
        df = pd.DataFrame([1, 2])
        assert_pdo_equal(df, df)
        mock_frame_equal.assert_called_once_with(df, df)

    @patch.object(pd.testing, "assert_series_equal")
    def test_should_map_to_series_equal(self, mock_series_equal):
        s = pd.Series([1, 2])
        assert_pdo_equal(s, s)
        mock_series_equal.assert_called_once_with(s, s)

    @patch.object(pd.testing, "assert_index_equal")
    def test_should_map_to_index_equal(self, mock_index_equal):
        i = pd.Index([1, 2])
        assert_pdo_equal(i, i)
        mock_index_equal.assert_called_once_with(i, i)
