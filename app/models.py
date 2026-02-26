"""
Pydantic models for the W-D Estimating Agent.
"""

from pydantic import BaseModel


class QuoteLineItem(BaseModel):
    product_id: str
    product_name: str
    size_label: str
    quantity: int
    base_unit_price: float
    glass_option: str
    glass_multiplier: float
    finish_option: str
    finish_surcharge: float
    addons: list[str]
    addon_total: float
    line_total: float


class QuoteRequest(BaseModel):
    client_name: str
    project_address: str
    items: list[dict]


class QuoteResult(BaseModel):
    quote_number: str
    client_name: str
    project_address: str
    line_items: list[QuoteLineItem]
    subtotal: float
    gst: float
    total: float


class UploadTakeoffRequest(BaseModel):
    """Simulated AI takeoff extraction from uploaded schedule."""
    filename: str
