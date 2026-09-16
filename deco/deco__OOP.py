"""Decorator pattern: wrap a component with extra behavior without changing it."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from time import perf_counter

logger = logging.getLogger(__name__)


def is_prime(number: int) -> bool:
    """Return True if ``number`` is a prime integer."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = int(number**0.5) + 1
    for element in range(3, limit, 2):
        if number % element == 0:
            return False
    return True


class Component(ABC):
    """Interface for work that can be wrapped by decorators."""

    @abstractmethod
    def execute(self, upper_bound: int) -> int:
        """Run the operation for integers in ``range(upper_bound)``."""
        ...


class PrimeCounter(Component):
    """Count how many prime numbers exist below ``upper_bound``."""

    def execute(self, upper_bound: int) -> int:
        return sum(1 for number in range(upper_bound) if is_prime(number))


class Decorator(Component):
    """Base wrapper that forwards calls to another ``Component``."""

    def __init__(self, wrapped: Component) -> None:
        """Store the component this decorator adds behavior around."""
        self._wrapped = wrapped

    def execute(self, upper_bound: int) -> int:
        """Delegate ``execute`` to the wrapped component."""
        return self._wrapped.execute(upper_bound)

    @property
    def wrapped_name(self) -> str:
        """Class name of the directly wrapped component."""
        return type(self._wrapped).__name__


class TimingDecorator(Decorator):
    """Log how long the wrapped ``execute`` call takes."""

    def execute(self, upper_bound: int) -> int:
        """Time the wrapped call, log the duration, and return its result."""
        started = perf_counter()
        value = super().execute(upper_bound)
        elapsed = perf_counter() - started
        logger.info(f"Execution of {self.wrapped_name} took {elapsed:.6f} seconds")
        return value


class LoggingDecorator(Decorator):
    """Log before and after the wrapped ``execute`` call."""

    def execute(self, upper_bound: int) -> int:
        """Log entry and exit around the wrapped call and return its result."""
        logger.info(f"Calling {self.wrapped_name} with upper_bound {upper_bound}")
        value = super().execute(upper_bound)
        logger.info(f"Finished calling {self.wrapped_name}")
        return value


def main() -> None:
    """Count primes below one million using logging and timing wrappers."""
    logging.basicConfig(level=logging.INFO)
    counter: Component = LoggingDecorator(TimingDecorator(PrimeCounter()))
    found = counter.execute(1_000_000)
    logger.info(f"Found {found} prime numbers")


if __name__ == "__main__":
    main()
