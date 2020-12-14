import pytest


class TestInit:
    class TestInit:
        def test_init_call_should_add_pandas_accessors(self):
            import pandas_addons as pda
            from pandas_addons.register import ACCESSORS

            pda.init()
            assert all(
                [
                    hasattr(pdo, accessor_name)
                    for accessor_name, pdos in ACCESSORS.items()
                    for pdo in pdos
                ]
            )

    class TestPandasAddons:
        def test_should_raise_with_incompatible_types(self):
            import pandas as pd

            import pandas_addons as pda

            @pda.register(pd.Series)
            def accessor(pdo):
                return pdo

            with pytest.raises(ValueError):
                pda.PandasAddons(pd.DataFrame([])).accessor()
            pd.testing.assert_series_equal(
                pd.Series([]), pda.PandasAddons(pd.Series([])).accessor()
            )

        def test_should_have_pda_accessor(self):
            import pandas as pd

            import pandas_addons as pda

            assert hasattr(pd.DataFrame, "pda")
            assert hasattr(pd.Series, "pda")
            assert hasattr(pd.Index, "pda")
