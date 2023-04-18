"""Class decorator to check method name length."""


def check_name_length(max_len=30):
    """Check method name length.

    Raises a `NameError` if one method name of a decoratoed class is
    longer than `max_len`.
    """
    def _check_name_length(cls):
        for name, obj in cls.__dict__.items():
            if callable(obj) and len(name) > max_len:
                msg = (f'name `{name}` too long,\n  ' + len('NameError') * ' ' +
                       f'found {len(name)} characters, only {max_len} are allowed')
                raise NameError(msg)
        return cls
    return _check_name_length