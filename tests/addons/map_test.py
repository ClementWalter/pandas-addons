from unittest.mock import patch, sentinel

import pandas as pd

from pandas_addons.addons.map import map


class TestMap:
    @patch.object(pd.Series, "map")
    def test_should_call_base_map(self, mock_map):
        map(pd.Series(dtype="object"), sentinel.args)
        mock_map.assert_called_once_with(sentinel.args)

    @patch("multiprocessing.pool.Pool.imap")
    def test_should_call_imap(self, mock_imap):
        map(pd.Series(dtype="object"), sentinel.args, parallel=True)
        mock_imap.assert_called_once_with(sentinel.args, [])
