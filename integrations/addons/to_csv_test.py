import pandas as pd
import pytest


class TestToCsv:
    @pytest.mark.parametrize("pandas_object", (pd.DataFrame, pd.Series))
    def test_should_write_same_file(self, pandas_object, tmp_path):
        pdo = pandas_object([1, 2])
        pdo.to_csv(tmp_path / "original.csv")

        # noinspection PyUnresolvedReferences
        import pandas_addons as pda

        pdo.pda.to_csv(tmp_path / "new.csv")
        assert (tmp_path / "original.csv").read_text() == (tmp_path / "new.csv").read_text()

    @pytest.mark.parametrize("pandas_object", (pd.DataFrame, pd.Series))
    def test_should_return_object(self, pandas_object, tmp_path):
        pdo = pandas_object([1, 2])

        # noinspection PyUnresolvedReferences
        import pandas_addons as pda

        pda.testing.assert_pdo_equal(pdo, pdo.pda.to_csv(tmp_path / "tmp.csv"))
