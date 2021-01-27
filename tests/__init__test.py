import pytest


@pytest.fixture
def pda():
    import pandas_addons as pda

    pda.init()

    yield pda

    pda.clear()


class TestInit:
    class TestInit:
        def test_init_call_should_add_pandas_accessors(self, pda):
            from pandas_addons.register import accessors

            assert all(
                [
                    hasattr(pdo, accessor_name)
                    for accessor_name, pdos in accessors.items()
                    for pdo in pdos
                ]
            )

    class TestClear:
        def test_should_remove_all_accessors(self, pda):
            from pandas_addons.register import accessors, original_accessor

            pda.clear()

            assert all(
                [
                    not hasattr(pdo, accessor_name)
                    or getattr(pdo, accessor_name) is original_accessor[(pdo, accessor_name)]
                    for accessor_name, pdos in accessors.items()
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

            s = pd.Series([], dtype="float64")
            pd.testing.assert_series_equal(s, pda.PandasAddons(s).accessor())

        def test_should_have_pda_accessor(self):
            import pandas as pd

            # noinspection PyUnresolvedReferences
            import pandas_addons as pda

            assert hasattr(pd.DataFrame, "pda")
            assert hasattr(pd.Series, "pda")
            assert hasattr(pd.Index, "pda")
