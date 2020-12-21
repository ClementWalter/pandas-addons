import pandas as pd


def assert_pdo_equal(pdo, *args, **kwargs):
    if isinstance(pdo, pd.DataFrame):
        return pd.testing.assert_frame_equal(pdo, *args, **kwargs)
    if isinstance(pdo, pd.Series):
        return pd.testing.assert_series_equal(pdo, *args, **kwargs)
    if isinstance(pdo, pd.Index):
        return pd.testing.assert_index_equal(pdo, *args, **kwargs)
    raise ValueError(f"Cannot fund pd.testing method for object of class {pdo.__class__.__name__}")
