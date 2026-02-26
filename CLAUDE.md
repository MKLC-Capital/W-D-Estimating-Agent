# CLAUDE.md — W-D Estimating Agent

## Project Overview

**W-D Estimating Agent** is an AI-powered estimating system for Blackline Structures' steel-framed windows and doors. It processes construction documents (window/door schedules, floor plans), extracts line items via AI, and generates priced quotes — all through a web interface styled to match the Blackline brand.

**Organization:** MKLC-Capital
**Repository:** `MKLC-Capital/W-D-Estimating-Agent`
**Client:** Blackline Structures (Queensland steel framing manufacturer)

## Project Structure

```
W-D-Estimating-Agent/
├── CLAUDE.md                    # This file — AI assistant guide
├── README.md                    # Project overview and setup
├── requirements.txt             # Python dependencies
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI application, routes
│   ├── models.py                # Pydantic data models
│   ├── products.py              # Product catalog (W&D types, sizes, pricing)
│   ├── estimator.py             # Pricing engine + AI takeoff simulation
│   ├── templates/
│   │   ├── base.html            # Shared layout (nav, footer, Tailwind config)
│   │   ├── index.html           # Landing page — product showcase
│   │   ├── quote.html           # Interactive quote builder
│   │   ├── upload.html          # AI takeoff upload page
│   │   └── result.html          # Quote result display
│   └── static/
│       └── style.css            # Additional styles (minimal)
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3 + FastAPI |
| Templates | Jinja2 |
| Frontend | Tailwind CSS (CDN), vanilla JavaScript |
| Data models | Pydantic v2 |
| Server | Uvicorn |

## Build & Run Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Start the development server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests (when added)
python -m pytest tests/

# Import check
python -c "from app.main import app; print('OK')"
```

## Key Modules

### `app/products.py`
Product catalog containing all window types (awning, casement, fixed, sliding), door types (hinged, sliding, bifold, pivot), glass options, powder coat finishes, and add-ons. Each product has multiple size options with base pricing in AUD.

### `app/estimator.py`
Pricing engine that calculates line items based on:
- Base product price (by type + size)
- Glass option multiplier (e.g., double-glazed = 1.65x)
- Finish surcharge (e.g., Custom RAL = +$150)
- Add-on items (e.g., flyscreen = +$185)
- Quantity

Also contains `simulate_ai_takeoff()` — a simulated AI extraction that returns realistic sample data as if parsed from a construction document. Replace with real AI integration later.

### `app/main.py`
FastAPI routes:
- `GET /` — Landing page (product showcase)
- `GET /quote` — Interactive quote builder
- `GET /upload` — AI takeoff upload page
- `GET /result` — Quote result display
- `POST /api/quote` — Generate a priced quote (JSON API)
- `POST /api/takeoff` — Simulate AI takeoff extraction (JSON API)
- `GET /api/products` — Full product catalog (JSON API)

### Templates
- `base.html` — Shared layout with Blackline branding (dark nav, gold accent, Inter font)
- `index.html` — Product showcase with SVG illustrations, pricing, glass/finish options
- `quote.html` — Interactive configurator (add line items, select options, submit)
- `upload.html` — File upload with animated AI processing steps
- `result.html` — Professional quote output with itemised table, GST, terms

## Development Conventions

### Git Workflow

- **Default branch:** `master`
- **Feature branches:** Descriptive names (e.g., `feature/document-parser`, `fix/pricing-calculation`)
- Imperative mood commit messages (e.g., "Add PDF schedule parser")
- One logical change per commit

### Code Style

- Python: follow standard conventions, type hints on function signatures
- Use domain-specific names: `takeoff_items`, `unit_price`, `glass_multiplier`, `line_total`
- Keep functions small and focused
- Templates: Jinja2 with Tailwind utility classes

### Testing

- Write tests for all pricing logic (critical path)
- Test the estimation engine with edge cases (zero quantity, unknown product IDs, boundary sizes)
- Tests should live in `tests/` directory

## Domain Context

| Term | Meaning |
|------|---------|
| **W-D** | Windows and Doors |
| **Takeoff** | Extracting quantities and specs from construction documents |
| **Schedule** | Table in construction docs listing window/door specs |
| **Quote / Estimate** | Priced output provided to a client |
| **Floor Plan** | Architectural drawing showing building layout |
| **GST** | Australian Goods and Services Tax (10%) |
| **BAL-40** | Bushfire Attack Level rating for construction in fire-prone areas |
| **Colorbond** | Australian steel colour range (Monument, Woodland Grey, Surfmist, etc.) |
| **IGU** | Insulated Glass Unit (double glazed) |
| **Low-E** | Low-emissivity glass coating for thermal performance |

## AI Assistant Guidelines

1. **Read before writing.** Always read existing files before modifying them.
2. **Stay focused.** Only make changes that are directly requested.
3. **Respect the domain.** Use construction/estimating terminology consistently.
4. **Test critical logic.** Pricing, measurement, and extraction logic must have tests.
5. **Keep it simple.** Build for the current requirement, not hypothetical future ones.
6. **Update this file.** When adding major components or changing patterns, update CLAUDE.md.
7. **Pricing accuracy.** Double-check all arithmetic in the estimator. Pricing bugs are high-impact.
8. **Australian context.** This is an Australian business — use AUD, metric units (mm), GST at 10%, Australian English spelling.

## Architecture Decisions

- **FastAPI + Jinja2** chosen for rapid prototyping with server-rendered pages and JSON APIs
- **Tailwind CSS via CDN** for styling without a build step
- **No database yet** — product catalog is in-memory (Python dicts). Migrate to DB when persistence is needed
- **Simulated AI takeoff** — `simulate_ai_takeoff()` returns hardcoded sample data. Replace with actual document parsing (e.g., OCR + LLM extraction) in production
- **Client-side quote state** — quote results stored in `sessionStorage` for the result page. Move to server-side sessions or DB for production
