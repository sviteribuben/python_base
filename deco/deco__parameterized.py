"""
Parameterized Decorators:
A decorator that accepts parameters.
"""

import logging
from functools import wraps
from typing import Any, Callable


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def repeat(num_times: int):
    """Decorator that repeats the function `num_times` times."""

    def decorator_repeat(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info(f"Repeating function {func.__name__} {num_times} times.")
            for _ in range(num_times):
                result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} repeated {num_times} times.")
            return result

        return wrapper

    return decorator_repeat


if __name__ == "__main__":

    @repeat(num_times=3)
    def greet(name: str) -> str:
        print(f"Hello, {name}!")

    greet("Sviter")
