import pandas as pd
import pytest


class TestConcat:
    @pytest.mark.parametrize("axis", (0, 1))
    def test_should_concat_on_axis(self, axis):
        input_dataframe = pd.DataFrame({"filepath": ["path/to/file_0", "path/to/file_1"]})

        # noinspection PyUnresolvedReferences
        import pandas_addons as pda

        pd.testing.assert_frame_equal(
            input_dataframe.pda.concat([input_dataframe], axis=axis),
            pd.concat([input_dataframe, input_dataframe], axis=axis),
        )
