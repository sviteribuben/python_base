# python-base

A personal notebook of Python concepts. Each topic is a small, runnable example —
not a library and not an application. The point is to make the idea readable in one file.

Requires **Python 3.14+**. Run examples with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync
```

## Run an example

```bash
uv run python deco/deco__OOP.py
uv run python deco/deco__parameterized.py
uv run python OOP_cls_vs_staticmethod.py
```

## Topics

| Path | Concept |
| --- | --- |
| `deco/deco__OOP.py` | GoF Decorator pattern via classes: `Component` / `Decorator` wrap a `PrimeCounter` with logging and timing; wrappers stack |
| `deco/deco__parameterized.py` | Function decorators: a plain `log_action` wrapper and a parameterized `repeat(num_times=...)` factory, both using `functools.wraps` |
| `OOP_cls_vs_staticmethod.py` | `@staticmethod` vs `@classmethod`: helpers that do not need `self`, vs factory methods that receive `cls` |

## Layout

One directory per idea when the topic has more than one file. When the same idea is shown more than one way:

- `topic__OOP.py` — classes / GoF-style
- `topic__fn.py` — functions, closures, or `functools`
- `topic.py` — a single canonical example

A lone file at the repo root is fine until a second variant appears; then it should move into its own folder.

Each example has a short module docstring (or comments that name the idea) and can be executed on its own.

## Tooling

Declared in `pyproject.toml`:

- [ruff](https://docs.astral.sh/ruff/) — lint and format
- [pytest](https://docs.pytest.org/) — tests when an example has logic worth locking in
- [ty](https://github.com/astral-sh/ty) — type checking
- [prek](https://pre-commit.com/) — pre-commit hooks
