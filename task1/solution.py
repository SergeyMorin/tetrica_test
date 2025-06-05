from inspect import signature


def strict(func):
    def wrapper(*args, **kwargs):
        sig_args = signature(func).bind(*args, **kwargs).arguments
        annotations = func.__annotations__
        for arg, value in sig_args.items():
            print(isinstance(value, annotations[arg]))
            if not isinstance(value, annotations[arg]):
                raise TypeError
        return func(*args, **kwargs)
    return wrapper
