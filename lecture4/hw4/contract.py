class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if raises is None:
                return
            elif raises is Any:
                try:
                    func(*args, **kwargs)
                except Exception as exc:
                    raise exc
            else:
                try:
                    func(*args, **kwargs)
                except Exception as exc:
                    if exc in raises:
                        raise exc
            if arg_types is not None:
                for k, v in enumerate(arg_types):
                    if None in args:
                        raise ContractError from TypeError
                    if v is Any:
                        break
                    elif not isinstance(args[k], v):
                        raise ContractError
            else:
                return
            if return_type is not None:
                if return_type is Any:
                    pass
                elif not isinstance(func(*args, **kwargs), return_type):
                    raise ContractError
            else:
                return
            print('ok')
        return wrapper
    return decorator
