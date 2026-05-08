# Autonomous Agent Guidelines

This document outlines the operational boundaries, tool usage policies, and safety protocols for autonomous agents working within the `data-continuum` repository.

## Core Directives
1. **Safety First**: Do not execute commands that destructively modify data, databases, or infrastructure without explicit user consent.
2. **Read Before Write**: Always investigate the existing architecture, codebase, and documentation before suggesting or making changes.
3. **Environment**: Keep context local. Do not perform work outside of the workspace directory unless explicitly requested.
4. **Iterative Verification**: Make small, verifiable changes. Use available testing tools to validate your changes incrementally.

## Development Workflow
- **Dependency Management**: Use `uv` for managing dependencies. Modify `pyproject.toml` appropriately when adding or removing packages.
- **Testing**: Run tests using `pytest` to ensure your changes do not break existing functionality.
- **Code Quality**: Ensure the code passes the `pre-commit` hooks. Check `.pre-commit-config.yaml` for active hooks.

## Best Practices
- **Documentation**: Automatically update relevant markdown files in `docs/` if your changes alter system architecture or APIs.
- **Tool Usage**: Prefer specialized tools (e.g., file readers, AST modifiers) over generic shell commands (e.g., `sed`, `awk`) for reliability.
- **Commit History**: When committing code, provide clear, descriptive commit messages summarizing the changes and their rationale.

## Project Specifics (Data-Continuum)
- The project integrates multiple domains including APIs, Airflow workflows, and ML components.
- Maintain consistency across boundaries: Ensure changes in one domain (e.g., database schemas) correctly propagate to dependent layers (e.g., API Pydantic models).
- Respect Docker environments: Test functionality keeping in mind that components are expected to run within containerized configurations defined in `docker-compose.yml`.
