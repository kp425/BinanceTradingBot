import functools
import logging

#prints asyc responses
def print_fn(func):
    @functools.wraps(func)
    async def _print_fn(*args, **kwargs):
        response = await func(*args, **kwargs)
        print("\n")
        print(response)
        print(response.status)
    return _print_fn


def setup_logging(level):
    levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
    }
    level = levels.get(level.lower())

    if level is None:
        raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")
    
    logging.basicConfig(level=level)
    logger = logging.getLogger(__name__)


