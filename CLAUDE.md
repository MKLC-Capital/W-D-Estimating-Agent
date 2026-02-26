# CLAUDE.md — W-D Estimating Agent

## Project Overview

**W-D Estimating Agent** is an AI-powered estimating system for construction window and door (W-D) takeoffs and pricing. The system processes construction documents (schedules, floor plans) and produces accurate quotes for window and door supply.

**Organization:** MKLC-Capital
**Repository:** `MKLC-Capital/W-D-Estimating-Agent`

## Repository Status

This project is in **early-stage development** (greenfield). The codebase is being built from scratch. When contributing, expect the structure below to evolve — update this file as the project grows.

## Project Structure

```
W-D-Estimating-Agent/
├── CLAUDE.md              # This file — AI assistant guide
├── README.md              # Project overview
└── (project files TBD)    # Architecture being established
```

As the project grows, the expected structure should follow a standard layout appropriate to the chosen tech stack (e.g., `src/`, `tests/`, `config/`, `docs/`).

## Development Conventions

### Git Workflow

- **Default branch:** `master`
- **Feature branches:** Use descriptive names (e.g., `feature/document-parser`, `fix/pricing-calculation`)
- Write clear, concise commit messages in imperative mood (e.g., "Add PDF schedule parser", not "Added PDF schedule parser")
- Keep commits focused — one logical change per commit
- Push feature branches and open PRs for review before merging to `master`

### Code Style

- Follow the conventions of whatever language/framework is adopted
- Prefer readability and simplicity over cleverness
- Use meaningful variable and function names that reflect the construction/estimating domain
- Keep functions small and focused on a single responsibility

### Testing

- Write tests for all business logic, especially pricing calculations and document parsing
- Tests should be runnable with a single command (document the command here as it is established)
- Aim for high coverage on critical paths: takeoff extraction, pricing rules, quote generation

### Documentation

- Update this `CLAUDE.md` file when adding new major components, changing project structure, or establishing new conventions
- Document public APIs and complex business logic inline
- Keep the README.md focused on user-facing setup and usage instructions

## Domain Context

Key terminology for AI assistants working on this project:

| Term | Meaning |
|------|---------|
| **W-D** | Windows and Doors |
| **Takeoff** | The process of extracting quantities and specifications from construction documents |
| **Schedule** | A table in construction documents listing window/door specs (sizes, types, quantities, hardware) |
| **Quote / Estimate** | The priced output provided to a client based on a takeoff |
| **Floor Plan** | Architectural drawing showing building layout; provides context for window/door placement |

## AI Assistant Guidelines

When working on this codebase:

1. **Read before writing.** Always read existing files before modifying them. Understand the current state.
2. **Stay focused.** Only make changes that are directly requested. Do not refactor or "improve" adjacent code.
3. **Respect the domain.** Use construction/estimating terminology consistently. Variable names like `window_schedule`, `takeoff_items`, `unit_price` are preferred over generic names.
4. **Test critical logic.** Any pricing, measurement, or extraction logic must have corresponding tests.
5. **Keep it simple.** Avoid over-engineering. Build for the current requirement, not hypothetical future ones.
6. **Update this file.** When you add a significant new component or establish a new pattern, add it to the relevant section of this CLAUDE.md.

## Build & Run Commands

> **Note:** To be filled in as the tech stack is established. Document all essential commands here:
>
> ```bash
> # Install dependencies
> # TBD
>
> # Run tests
> # TBD
>
> # Start the application
> # TBD
>
> # Lint / format
> # TBD
> ```

## Architecture Decisions

Document key architecture choices here as they are made:

- *(No decisions recorded yet — update as the project develops)*
