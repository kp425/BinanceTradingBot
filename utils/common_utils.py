import functools

#prints asyc responses
def print_fn(func):
    @functools.wraps(func)
    async def _print_fn(*args, **kwargs):
        response = await func(*args, **kwargs)
        print("\n")
        print(response)
        print(response.status)
    return _print_fn
