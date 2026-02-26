# W-D Estimating Agent

AI-powered estimating system for Blackline Structures' steel-framed windows and doors. Upload a window/door schedule, and the AI agent extracts every line item, matches to the product catalogue, and generates a priced quote.

## Features

- **Product Showcase** — Browse steel-framed windows (awning, casement, fixed, sliding) and doors (hinged, sliding, bifold, pivot) with pricing from the catalogue
- **Interactive Quote Builder** — Select products, sizes, glass options, finishes, and add-ons. Pricing updates live
- **AI Takeoff** — Upload a window/door schedule (PDF/image) and the AI agent extracts items and generates a quote automatically
- **Professional Quote Output** — Itemised pricing with GST, terms and conditions, print-ready format

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python -m uvicorn app.main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Pages

| Route | Description |
|-------|-------------|
| `/` | Landing page — product showcase, pricing, options |
| `/quote` | Interactive quote builder |
| `/upload` | AI takeoff — upload schedule for automatic extraction |
| `/result` | Generated quote with full pricing breakdown |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/quote` | Generate a priced quote from line items |
| `POST` | `/api/takeoff` | Simulate AI extraction from uploaded schedule |
| `GET` | `/api/products` | Full product catalogue (JSON) |

## Tech Stack

- **Backend:** Python 3 / FastAPI
- **Frontend:** Jinja2 templates, Tailwind CSS, vanilla JS
- **Pricing Engine:** Custom estimator with glass multipliers, finish surcharges, add-ons, GST

## Product Catalogue

### Windows
- Steel Awning Window (from $485)
- Steel Casement Window (from $595)
- Steel Fixed Window (from $345)
- Steel Sliding Window (from $795)

### Doors
- Steel Hinged Door (from $1,650)
- Steel Sliding Door (from $2,450)
- Steel Bifold Door (from $3,200)
- Steel Pivot Door (from $3,800)

### Customisation
- 8 glass options (clear, laminated, Low-E, double glazed, acoustic, tinted, obscure)
- 7 powder coat finishes (Matt Black, Satin Black, Colorbond colours, Custom RAL)
- 6 add-ons (fly screens, security mesh, premium hardware, sidelights, transoms, BAL-40)
