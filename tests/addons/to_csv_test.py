from unittest.mock import MagicMock, patch, sentinel

from pandas_addons.addons.to_csv import BASE_TO_CSV, to_csv


@patch.dict(BASE_TO_CSV, {sentinel.__class__: MagicMock()}, clear=True)
class TestToCsv:
    def test_should_call_base_to_csv_method_with_given_args_and_kwargs(self):
        to_csv(sentinel, sentinel.arg, kwarg=sentinel.kwarg)
        BASE_TO_CSV[sentinel.__class__].assert_called_once_with(
            sentinel, sentinel.arg, kwarg=sentinel.kwarg
        )

    def test_should_return_original_object(self):
        assert to_csv(sentinel) == sentinel
