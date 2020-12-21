from pandas_addons.register import DEFAULT_PANDAS_OBJECTS, register

BASE_TO_CSV = {
    pandas_object: getattr(pandas_object, "to_csv")
    for pandas_object in DEFAULT_PANDAS_OBJECTS
    if hasattr(pandas_object, "to_csv")
}


@register(*BASE_TO_CSV.keys())
def to_csv(pandas_object, *args, **kwargs):
    BASE_TO_CSV[pandas_object.__class__](pandas_object, *args, **kwargs)
    return pandas_object
