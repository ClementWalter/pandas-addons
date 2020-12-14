from pandas_addons.register import register


@register
def assert_(pandas_object, func, *args, error_type=AssertionError):
    try:
        cond = bool(func(pandas_object))
    except ValueError as original_error:
        raise ValueError(
            (
                "Cannot cast function output to bool, did you forget to add `.all()`, `.any()` or `.empty`?\n"
                "Original output:\n"
                f"{func(pandas_object)}"
            )
        ) from original_error
    if not cond:
        raise error_type(*[arg(pandas_object) if callable(arg) else arg for arg in args])
    return pandas_object
