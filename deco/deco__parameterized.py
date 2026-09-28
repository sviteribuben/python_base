"""
Parameterized Decorators:
A decorator that accepts parameters.
"""

import logging
from functools import wraps
from typing import Any, Callable


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def log_action(func: Callable[..., Any]) -> Callable[..., Any]:
    """Simple decorator for logging the function call"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info(f"--- Start function {func.__name__} ---")
        result = func(*args, **kwargs)
        logger.info(f"--- End function {func.__name__}. Result: {result} ---")
        return result
    return wrapper


def repeat(num_times: int):
    """Decorator that repeats the function `num_times` times."""

    def decorator_repeat(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


if __name__ == "__main__":

    @repeat(num_times=3)
    @log_action
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    result = greet("Sviter")
    print(f"Final print in console: {result}")