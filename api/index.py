"""Vercel serverless entry point — re-exports the FastAPI app."""

import os
import sys
from pathlib import Path

# Ensure the project root is on sys.path so the `app` package is importable.
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

try:
    from app.main import app  # noqa: E402
except Exception as exc:
    # If import fails, serve a diagnostic page so we can see the real error
    # instead of a generic FUNCTION_INVOCATION_FAILED.
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse

    app = FastAPI()

    _error_msg = (
        f"Import failed: {type(exc).__name__}: {exc}\n\n"
        f"sys.path: {sys.path}\n\n"
        f"project root: {_project_root}\n"
        f"project root exists: {os.path.isdir(_project_root)}\n"
        f"project root contents: {os.listdir(_project_root) if os.path.isdir(_project_root) else 'N/A'}\n\n"
        f"app dir exists: {os.path.isdir(os.path.join(_project_root, 'app'))}\n"
        f"app dir contents: {os.listdir(os.path.join(_project_root, 'app')) if os.path.isdir(os.path.join(_project_root, 'app')) else 'N/A'}\n"
    )

    @app.get("/{path:path}")
    async def _diagnostic(path: str):
        return PlainTextResponse(_error_msg, status_code=500)
