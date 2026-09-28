# python-base

A personal notebook of Python concepts. Each folder is one topic with small, runnable
examples. This is not a library or an application — the point is to make the pattern
readable in one file.

Requires **Python 3.14+**. Examples are run with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync
```

## Run an example

```bash
uv run python deco/deco__OOP.py
uv run python deco/deco__parameterized.py
```

## Topics

| Folder | File | Concept |
| --- | --- | --- |
| `deco/` | `deco__OOP.py` | GoF Decorator pattern via classes: `Component` / `Decorator` wrap a `PrimeCounter` with logging and timing, and the wrappers stack |
| `deco/` | `deco__parameterized.py` | Function decorators: a plain `log_action` decorator and a parameterized `repeat(num_times=...)` factory, both using `functools.wraps` |

Each file has a short module docstring, type hints on public functions, and a
`main()` (or a `__main__` block) so it can be executed on its own.

## Tooling

Declared in `pyproject.toml`:

- [ruff](https://docs.astral.sh/ruff/) — lint and format
- [pytest](https://docs.pytest.org/) — tests when an example has logic worth locking in
- [ty](https://github.com/astral-sh/ty) — type checking
- [prek](https://pre-commit.com/) — pre-commit hooks
