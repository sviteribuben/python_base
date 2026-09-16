# AGENTS.md

This repo is a personal notebook of Python concepts, not a production application. Each folder is a self-contained topic with small, runnable examples.

## Project

- Name: `python-base`
- Python: 3.14 (`requires-python = ">=3.14"`)
- Package manager: [uv](https://docs.astral.sh/uv/)
- Tooling already in `pyproject.toml`: `ruff`, `pytest`, `ty`

Run examples with `uv run python path/to/file.py`. Prefer that over activating `.venv` by hand.

## Layout

Put one concept in one directory. Name the directory after the idea (`deco`, `iterators`, `contextmgr`).

If the same idea is shown more than one way, use a suffix:

- `topic__OOP.py` — class-based / GoF-style
- `topic__fn.py` — functions, closures, or `functools`
- `topic.py` — only when there is a single canonical example

Keep files focused. Do not dump unrelated patterns into an existing topic folder.

## How to add a concept

1. Create a new folder at the repo root (or next to related topics).
2. Add a short module docstring that names the concept in one sentence.
3. Include a `main()` plus `if __name__ == "__main__":` so the file can be run.
4. Prefer a tiny, complete demo over a framework or extra packages.
5. Add tests under the same folder or `tests/` only when the example has logic worth locking in (algorithms, edge cases). Skip tests for pure illustration.

## Code style

- Type-hint public functions, methods, and class attributes.
- Add short docstrings on modules, classes, and non-obvious functions. Do not narrate every line.
- Use f-strings in logging and user-facing messages (`logger.info(f"Found {found} primes")`).
- Use a module logger: `logger = logging.getLogger(__name__)`.
- Keep examples modern for 3.14 (`from __future__ import annotations` is fine).
- Stay readable over clever. Teach the concept; do not hide it behind helpers unless the helper *is* the lesson.
- Match existing naming in a folder when extending it.

## What not to do

- Do not turn this into an installable library, CLI product, or app scaffold unless asked.
- Do not add dependencies unless the concept requires them. Prefer the standard library.
- Do not commit `.venv/`, `.ruff_cache/`, or secrets.
- Do not rewrite unrelated topic folders when adding a new one.
- Do not create commits or push to GitHub unless the user asks.

## Agent workflow

When the user asks to save a concept: implement a small runnable example, keep the folder isolated, and explain the idea in code and docstrings rather than a long README. A one-line module docstring is enough unless they request more docs.

When fixing or refactoring: preserve the teaching goal of the file. If it is an OOP Decorator demo, keep the pattern visible.
