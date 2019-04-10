# flake8: noqa
from .env import data_path, src_path

try:    # Fake load_or_build to make `econtools` optional
    from econtools import load_or_build
except ImportError:
    from functools import wraps
    def load_or_build(raw_filepath):
        def actualDecorator(builder):
            @wraps(builder)
            def wrapped(*args, **kwargs):
                r = builder(*args, **kwargs)
                return r
            return wrapped
        return actualDecorator
