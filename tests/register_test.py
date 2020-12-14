import itertools
from unittest.mock import patch

import pytest

from pandas_addons.register import ACCESSORS, DEFAULT_PANDAS_OBJECTS, register


class TestRegister:
    def test_should_return_input_function(self):
        def accessor():
            pass

        assert accessor == register()(accessor)

    @patch.dict(ACCESSORS, {}, clear=True)
    def test_should_use_default_value_when_no_args(self):
        def accessor():
            pass

        register()(accessor)

        assert ACCESSORS == {"accessor": {pdo: accessor for pdo in DEFAULT_PANDAS_OBJECTS}}

    @patch.dict(ACCESSORS, {}, clear=True)
    def test_should_register_when_register_is_called_on_decorated(self):
        def accessor():
            pass

        register(accessor)

        assert ACCESSORS == {"accessor": {pdo: accessor for pdo in DEFAULT_PANDAS_OBJECTS}}

    @patch.dict(ACCESSORS, {}, clear=True)
    @pytest.mark.parametrize(
        "pandas_objects",
        itertools.chain.from_iterable(
            itertools.combinations(DEFAULT_PANDAS_OBJECTS, i + 1)
            for i in range(len(DEFAULT_PANDAS_OBJECTS))
        ),
    )
    def test_should_register_given_pandas_object(self, pandas_objects):
        def accessor():
            pass

        register(*pandas_objects)(accessor)
        assert ACCESSORS == {"accessor": {pdo: accessor for pdo in pandas_objects}}
