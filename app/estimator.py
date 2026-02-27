"""
Estimation engine for W-D Estimating Agent.

Calculates pricing for window and door configurations based on:
- Base product price (by type and size)
- Glass option multiplier
- Finish surcharge
- Add-on items
- Quantity
"""

from __future__ import annotations

import random
import string
from datetime import datetime

from app.models import QuoteLineItem, QuoteResult
from app.products import (
    ADDON_OPTIONS,
    FINISH_OPTIONS,
    GLASS_OPTIONS,
    get_product_by_id,
)

GST_RATE = 0.10  # 10% Australian GST


def _generate_quote_number() -> str:
    """Generate a quote reference like BLS-WD-250226-A3X."""
    date_part = datetime.now().strftime("%y%m%d")
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"BLS-WD-{date_part}-{random_part}"


def _find_glass(glass_id: str) -> dict | None:
    for g in GLASS_OPTIONS:
        if g["id"] == glass_id:
            return g
    return None


def _find_finish(finish_id: str) -> dict | None:
    for f in FINISH_OPTIONS:
        if f["id"] == finish_id:
            return f
    return None


def _find_addon(addon_id: str) -> dict | None:
    for a in ADDON_OPTIONS:
        if a["id"] == addon_id:
            return a
    return None


def calculate_line_item(
    product_id: str,
    size_index: int,
    quantity: int,
    glass_id: str = "laminated-6.38mm",
    finish_id: str = "matt-black",
    addon_ids: list[str] | None = None,
) -> QuoteLineItem:
    """Calculate a single line item price."""
    product = get_product_by_id(product_id)
    if not product:
        raise ValueError(f"Unknown product: {product_id}")

    if size_index < 0 or size_index >= len(product["sizes"]):
        raise ValueError(f"Invalid size index {size_index} for {product_id}")

    size = product["sizes"][size_index]
    base_price = size["base_price"]

    glass = _find_glass(glass_id) or GLASS_OPTIONS[0]
    finish = _find_finish(finish_id) or FINISH_OPTIONS[0]

    addon_ids = addon_ids or []
    addon_total = 0.0
    valid_addons = []
    for aid in addon_ids:
        addon = _find_addon(aid)
        if addon and product["category"] in addon["applies_to"]:
            addon_total += addon["price"]
            valid_addons.append(addon["name"])

    unit_price = (base_price * glass["multiplier"]) + finish["surcharge"] + addon_total
    line_total = unit_price * quantity

    return QuoteLineItem(
        product_id=product_id,
        product_name=product["name"],
        size_label=size["label"],
        quantity=quantity,
        base_unit_price=base_price,
        glass_option=glass["name"],
        glass_multiplier=glass["multiplier"],
        finish_option=finish["name"],
        finish_surcharge=finish["surcharge"],
        addons=valid_addons,
        addon_total=addon_total,
        line_total=round(line_total, 2),
    )


def generate_quote(
    client_name: str,
    project_address: str,
    items: list[dict],
) -> QuoteResult:
    """
    Generate a full quote from a list of item specs.

    Each item dict should contain:
        product_id, size_index, quantity, glass_id, finish_id, addon_ids
    """
    line_items = []
    for item in items:
        li = calculate_line_item(
            product_id=item["product_id"],
            size_index=item.get("size_index", 0),
            quantity=item.get("quantity", 1),
            glass_id=item.get("glass_id", "laminated-6.38mm"),
            finish_id=item.get("finish_id", "matt-black"),
            addon_ids=item.get("addon_ids", []),
        )
        line_items.append(li)

    subtotal = round(sum(li.line_total for li in line_items), 2)
    gst = round(subtotal * GST_RATE, 2)
    total = round(subtotal + gst, 2)

    return QuoteResult(
        quote_number=_generate_quote_number(),
        client_name=client_name,
        project_address=project_address,
        line_items=line_items,
        subtotal=subtotal,
        gst=gst,
        total=total,
    )


# --- Simulated AI Takeoff ---

SAMPLE_TAKEOFF_RESULTS = [
    {
        "product_id": "awning-window",
        "size_index": 2,
        "quantity": 6,
        "glass_id": "low-e",
        "finish_id": "matt-black",
        "addon_ids": ["flyscreen"],
        "extracted_note": "W01 — Awning 1200x900 (Bedrooms 1-3, Ensuite, Bathroom, Laundry)",
    },
    {
        "product_id": "fixed-window",
        "size_index": 4,
        "quantity": 2,
        "glass_id": "double-glazed-low-e",
        "finish_id": "matt-black",
        "addon_ids": [],
        "extracted_note": "W02 — Fixed 2400x1500 (Living Room feature windows)",
    },
    {
        "product_id": "sliding-window",
        "size_index": 2,
        "quantity": 3,
        "glass_id": "low-e",
        "finish_id": "monument",
        "addon_ids": ["flyscreen", "security-mesh"],
        "extracted_note": "W03 — Sliding 2400x1200 3-panel (Kitchen, Family, Study)",
    },
    {
        "product_id": "casement-window",
        "size_index": 1,
        "quantity": 2,
        "glass_id": "obscure",
        "finish_id": "matt-black",
        "addon_ids": ["flyscreen"],
        "extracted_note": "W04 — Casement 900x1200 (WC, Powder Room)",
    },
    {
        "product_id": "hinged-door",
        "size_index": 2,
        "quantity": 1,
        "glass_id": "laminated-6.38mm",
        "finish_id": "matt-black",
        "addon_ids": ["hardware-upgrade", "sidelight"],
        "extracted_note": "D01 — Double Hinged Entry 1640x2040 (Front Entry)",
    },
    {
        "product_id": "sliding-door",
        "size_index": 3,
        "quantity": 1,
        "glass_id": "double-glazed-low-e",
        "finish_id": "matt-black",
        "addon_ids": ["security-mesh"],
        "extracted_note": "D02 — Sliding 4200x2400 3-panel (Rear Alfresco)",
    },
    {
        "product_id": "bifold-door",
        "size_index": 2,
        "quantity": 1,
        "glass_id": "double-glazed",
        "finish_id": "matt-black",
        "addon_ids": [],
        "extracted_note": "D03 — Bifold 3600x2400 4-panel (Outdoor Living)",
    },
]


def simulate_ai_takeoff(filename: str) -> dict:
    """
    Simulate AI extraction from an uploaded window/door schedule.
    Returns extracted line items as if an AI parsed the construction document.
    """
    return {
        "filename": filename,
        "status": "extracted",
        "confidence": 0.94,
        "extracted_items": SAMPLE_TAKEOFF_RESULTS,
        "summary": {
            "total_windows": 13,
            "total_doors": 3,
            "unique_types": 7,
        },
    }
