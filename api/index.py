"""Vercel serverless entry point — re-exports the FastAPI app."""

import sys
from pathlib import Path

# Ensure the project root is on the Python path so `app` package is importable.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.main import app  # noqa: E402

# Vercel's @vercel/python runtime detects this ASGI app automatically.
handler = app
