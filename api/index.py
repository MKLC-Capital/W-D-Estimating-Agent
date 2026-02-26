"""Vercel serverless entry point — re-exports the FastAPI app."""

from app.main import app

# Vercel's @vercel/python runtime detects this ASGI app automatically.
handler = app
