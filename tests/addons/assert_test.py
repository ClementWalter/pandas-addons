from unittest.mock import MagicMock, sentinel

import pytest

from pandas_addons.addons.assert_ import assert_
from pandas_addons.register import DEFAULT_PANDAS_OBJECTS


class TestAssert:
    class TestAssert:
        @pytest.mark.parametrize("pandas_object", DEFAULT_PANDAS_OBJECTS)
        def test_should_raise_value_error_when_bool_fails(self, pandas_object):
            with pytest.raises(ValueError):
                assert_(pandas_object([], dtype="float64"), lambda x: x)

        def test_should_raise_on_failure(self):
            with pytest.raises(AssertionError):
                assert_(sentinel.pandas_object, lambda x: False)

        def test_should_call_args_on_raise_on_failure(self):
            arg = MagicMock()
            with pytest.raises(AssertionError):
                assert_(sentinel.pandas_object, lambda x: False, arg)
            arg.assert_called_once_with(sentinel.pandas_object)

        def test_should_return_original_object_on_success(self):
            assert assert_(sentinel.pandas_object, lambda x: True) == sentinel.pandas_object
