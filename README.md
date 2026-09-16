# python-base

A personal notebook of Python concepts. Each folder is one topic with small, runnable examples. This is not a library or an application.

Requires **Python 3.14+**. Examples are run with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync
```

## Run an example

```bash
uv run python deco/deco__OOP.py
```

## Topics

| Folder | File | Concept |
| --- | --- | --- |
| `deco/` | `deco__OOP.py` | Decorator pattern (class-based): wrap an object with extra behavior without changing it |

## Layout

One directory per idea. When the same idea is shown more than one way:

- `topic__OOP.py` — classes / GoF-style
- `topic__fn.py` — functions, closures, or `functools`
- `topic.py` — a single canonical example

Each file has a short module docstring and a `main()` so it can be executed on its own.

## Tooling

Declared in `pyproject.toml`:

- [ruff](https://docs.astral.sh/ruff/) — lint and format
- [pytest](https://docs.pytest.org/) — tests when an example has logic worth locking in
- [ty](https://github.com/astral-sh/ty) — type checking
