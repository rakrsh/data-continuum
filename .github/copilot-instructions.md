# GitHub Copilot Instructions

These are the instructions for GitHub Copilot and other AI assistants working in this repository.

## General Guidelines
- Follow the existing code style and conventions present in the repository.
- Write clean, concise, and self-documenting code.
- Prefer explicit over implicit implementations.
- Avoid introducing unnecessary external dependencies.

## Python Specifics
- **Type Hints**: Use Type Hints (PEP 484) for all function arguments and return values.
- **Formatting**: Adhere to PEP 8 standards. Use `black` or `ruff` for formatting and linting.
- **Testing**: Write unit tests using `pytest` and `httpx`. Ensure new tests pass the CI unit test workflow defined in `.github/workflows/unit-tests.yml`.
- **Documentation**: Include proper docstrings (Google or NumPy style) for classes, methods, and complex functions.
- **Logging**: Prioritize clear error handling and `logging` over basic `print` statements.

## Architecture and Configuration
- **Dependencies**: Keep the `pyproject.toml` and lockfiles (`uv.lock`) synchronized when dependencies are modified.
- **Microservices**: This project utilizes a containerized architecture. Ensure all new logic is Docker-friendly and respects service boundaries.
- **Documentation**: Ensure any changes to logic or architecture are reflected in the `docs/` directory or relevant `README.md` files.
- **Comprehensive Updates**: Any change in source code should also prompt a check to update the architecture diagram (`docs/architecture.md`), Copilot instructions (`.github/copilot-instructions.md`), `AGENTS.md`, pre-commit hooks, tests, and documentation as appropriate.
- **CI Workflows**: When modifying, adding, or deleting dependencies/components, always consider updating the corresponding CI workflows (e.g., `unit-tests.yml`, `security.yml`) to ensure comprehensive coverage, including security and vulnerability checks.
