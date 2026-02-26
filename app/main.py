"""
W-D Estimating Agent — FastAPI Application

AI-powered estimating system for Blackline Structures' steel-framed
windows and doors. Handles product catalog display, interactive quote
building, and simulated AI takeoff extraction.
"""

import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.estimator import generate_quote, simulate_ai_takeoff
from app.models import QuoteRequest, UploadTakeoffRequest
from app.products import (
    ADDON_OPTIONS,
    DOOR_TYPES,
    FINISH_OPTIONS,
    GLASS_OPTIONS,
    WINDOW_TYPES,
    get_all_products,
)

app = FastAPI(
    title="W-D Estimating Agent",
    description="AI estimating system for Blackline Structures windows and doors",
    version="0.1.0",
)

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# ──────────────────────────────────────────────
# Page routes
# ──────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Landing page — product showcase."""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "windows": WINDOW_TYPES,
        "doors": DOOR_TYPES,
        "glass_options": GLASS_OPTIONS,
        "finish_options": FINISH_OPTIONS,
        "addon_options": ADDON_OPTIONS,
    })


@app.get("/quote", response_class=HTMLResponse)
async def quote_builder(request: Request):
    """Interactive quote builder page."""
    return templates.TemplateResponse("quote.html", {
        "request": request,
        "products_json": json.dumps(get_all_products()),
        "glass_json": json.dumps(GLASS_OPTIONS),
        "finish_json": json.dumps(FINISH_OPTIONS),
        "addon_json": json.dumps(ADDON_OPTIONS),
    })


@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    """AI takeoff upload page."""
    return templates.TemplateResponse("upload.html", {
        "request": request,
        "glass_json": json.dumps(GLASS_OPTIONS),
    })


@app.get("/result", response_class=HTMLResponse)
async def result_page(request: Request):
    """Quote result display page."""
    return templates.TemplateResponse("result.html", {
        "request": request,
    })


# ──────────────────────────────────────────────
# API routes
# ──────────────────────────────────────────────

@app.post("/api/quote")
async def api_generate_quote(payload: QuoteRequest):
    """Generate a priced quote from selected line items."""
    result = generate_quote(
        client_name=payload.client_name,
        project_address=payload.project_address,
        items=payload.items,
    )
    return result.model_dump()


@app.post("/api/takeoff")
async def api_takeoff(payload: UploadTakeoffRequest):
    """Simulate AI takeoff extraction from an uploaded schedule."""
    result = simulate_ai_takeoff(payload.filename)
    return result


@app.get("/api/products")
async def api_products():
    """Return the full product catalog."""
    return {
        "windows": WINDOW_TYPES,
        "doors": DOOR_TYPES,
        "glass_options": GLASS_OPTIONS,
        "finish_options": FINISH_OPTIONS,
        "addon_options": ADDON_OPTIONS,
    }
