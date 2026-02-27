"""Vercel serverless entry point — re-exports the FastAPI app."""

import os
import sys
import traceback

# Try multiple possible locations for the project root.
# Vercel's Lambda environment may place files differently.
_this_dir = os.path.dirname(os.path.abspath(__file__))
_candidates = [
    os.path.dirname(_this_dir),          # ../  (standard: api/ -> project root)
    "/var/task",                          # Vercel Lambda default
    "/var/task/user",                     # Vercel alternative
    os.getcwd(),                         # working directory
    _this_dir,                           # same directory (if flat)
]

for _path in _candidates:
    if os.path.isdir(os.path.join(_path, "app")) and _path not in sys.path:
        sys.path.insert(0, _path)

try:
    from app.main import app  # noqa: E402
except Exception as exc:
    # If import fails, serve a diagnostic page with the real error
    # instead of a generic FUNCTION_INVOCATION_FAILED.
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse

    app = FastAPI()

    _tb = traceback.format_exc()
    _diag_parts = [
        f"IMPORT ERROR: {type(exc).__name__}: {exc}",
        f"\nTraceback:\n{_tb}",
        f"\nsys.path: {sys.path}",
        f"\ncwd: {os.getcwd()}",
        f"\n__file__: {__file__}",
        f"\nthis_dir: {_this_dir}",
    ]

    # List contents of every candidate directory
    for _p in _candidates:
        _exists = os.path.isdir(_p)
        _contents = sorted(os.listdir(_p)) if _exists else "DOES NOT EXIST"
        _diag_parts.append(f"\n{_p}/ -> {_contents}")
        # Check for app subdirectory
        _app_dir = os.path.join(_p, "app")
        if os.path.isdir(_app_dir):
            _diag_parts.append(f"  {_app_dir}/ -> {sorted(os.listdir(_app_dir))}")

    _error_msg = "\n".join(_diag_parts)

    @app.get("/{path:path}")
    async def _diagnostic(path: str):
        return PlainTextResponse(_error_msg, status_code=500)
