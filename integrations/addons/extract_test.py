import pandas as pd


class TestExtract:
    def test_should_extract_and_assign_series(self):
        input_dataframe = pd.DataFrame({"filepath": ["path/to/file_0", "path/to/file_1"]})

        # noinspection PyUnresolvedReferences
        import pandas_addons as pda

        output_dataframe = input_dataframe.pda.extract(
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
