"""
Product catalog for Blackline Structures — Windows and Doors.

All pricing in AUD. Products represent steel-framed window and door systems
manufactured by Blackline for residential and commercial construction.
"""

WINDOW_TYPES = [
    {
        "id": "awning-window",
        "name": "Steel Awning Window",
        "category": "windows",
        "description": "Top-hinged steel-framed awning window. Ideal for ventilation while maintaining weather protection. Powder-coated steel frame with thermally broken profiles.",
        "features": ["Powder-coated steel frame", "Thermally broken profile", "6.38mm laminated glass standard", "Multi-point locking", "Fly screen compatible"],
        "sizes": [
            {"label": "600 x 600mm", "width": 600, "height": 600, "base_price": 485.00},
            {"label": "900 x 900mm", "width": 900, "height": 900, "base_price": 625.00},
            {"label": "1200 x 900mm", "width": 1200, "height": 900, "base_price": 745.00},
            {"label": "1500 x 1200mm", "width": 1500, "height": 1200, "base_price": 920.00},
            {"label": "1800 x 1200mm", "width": 1800, "height": 1200, "base_price": 1085.00},
        ],
        "image_placeholder": "awning-window",
    },
    {
        "id": "casement-window",
        "name": "Steel Casement Window",
        "category": "windows",
        "description": "Side-hinged casement window with slimline steel frame. Maximum glass area with clean architectural lines. Available in single or double sash configurations.",
        "features": ["Slimline steel profile", "Single or double sash", "Concealed hinges", "Low-E glass option", "BAL-40 bushfire rated option"],
        "sizes": [
            {"label": "600 x 1200mm", "width": 600, "height": 1200, "base_price": 595.00},
            {"label": "900 x 1200mm", "width": 900, "height": 1200, "base_price": 735.00},
            {"label": "1200 x 1500mm", "width": 1200, "height": 1500, "base_price": 895.00},
            {"label": "1500 x 1500mm", "width": 1500, "height": 1500, "base_price": 1050.00},
            {"label": "1800 x 1800mm", "width": 1800, "height": 1800, "base_price": 1320.00},
        ],
        "image_placeholder": "casement-window",
    },
    {
        "id": "fixed-window",
        "name": "Steel Fixed Window",
        "category": "windows",
        "description": "Non-operable fixed panel with ultra-slim steel frame for maximum light and uninterrupted views. Perfect for feature walls and highlight windows.",
        "features": ["Ultra-slim 35mm steel frame", "Maximum glass area", "Double glazed option", "Custom shapes available", "Structural silicone glazing"],
        "sizes": [
            {"label": "600 x 600mm", "width": 600, "height": 600, "base_price": 345.00},
            {"label": "900 x 1200mm", "width": 900, "height": 1200, "base_price": 485.00},
            {"label": "1200 x 1500mm", "width": 1200, "height": 1500, "base_price": 620.00},
            {"label": "1800 x 1200mm", "width": 1800, "height": 1200, "base_price": 710.00},
            {"label": "2400 x 1500mm", "width": 2400, "height": 1500, "base_price": 985.00},
        ],
        "image_placeholder": "fixed-window",
    },
    {
        "id": "sliding-window",
        "name": "Steel Sliding Window",
        "category": "windows",
        "description": "Horizontal sliding steel-framed window. Smooth operation on stainless steel rollers. Available in 2, 3, or 4 panel configurations.",
        "features": ["Stainless steel rollers", "Multi-panel configurations", "Flush track option", "Security mesh compatible", "Acoustic glass option"],
        "sizes": [
            {"label": "1200 x 900mm (2-panel)", "width": 1200, "height": 900, "base_price": 795.00},
            {"label": "1800 x 1200mm (2-panel)", "width": 1800, "height": 1200, "base_price": 1050.00},
            {"label": "2400 x 1200mm (3-panel)", "width": 2400, "height": 1200, "base_price": 1380.00},
            {"label": "3000 x 1500mm (3-panel)", "width": 3000, "height": 1500, "base_price": 1720.00},
            {"label": "3600 x 1800mm (4-panel)", "width": 3600, "height": 1800, "base_price": 2250.00},
        ],
        "image_placeholder": "sliding-window",
    },
]

DOOR_TYPES = [
    {
        "id": "hinged-door",
        "name": "Steel Hinged Door",
        "category": "doors",
        "description": "Single or double hinged entry door with bold steel frame. Statement piece for residential and commercial entries. Fully glazed or panel options.",
        "features": ["Heavy-duty steel frame", "3-point locking system", "Stainless steel hinges", "Glazed or panel infill", "Threshold options"],
        "sizes": [
            {"label": "820 x 2040mm (Single)", "width": 820, "height": 2040, "base_price": 1650.00},
            {"label": "920 x 2040mm (Single)", "width": 920, "height": 2040, "base_price": 1780.00},
            {"label": "1640 x 2040mm (Double)", "width": 1640, "height": 2040, "base_price": 2950.00},
            {"label": "1840 x 2040mm (Double)", "width": 1840, "height": 2040, "base_price": 3150.00},
            {"label": "2100 x 2400mm (Double, oversized)", "width": 2100, "height": 2400, "base_price": 4200.00},
        ],
        "image_placeholder": "hinged-door",
    },
    {
        "id": "sliding-door",
        "name": "Steel Sliding Door",
        "category": "doors",
        "description": "Large-format sliding steel door system. Panoramic views with industrial-strength steel framing. Smooth glide operation for openings up to 6m wide.",
        "features": ["Openings up to 6000mm", "Top-hung or bottom-rolling", "Slim interlock profiles", "Integrated blinds option", "Flush floor track"],
        "sizes": [
            {"label": "1800 x 2100mm (2-panel)", "width": 1800, "height": 2100, "base_price": 2450.00},
            {"label": "2400 x 2100mm (2-panel)", "width": 2400, "height": 2100, "base_price": 3100.00},
            {"label": "3000 x 2400mm (3-panel)", "width": 3000, "height": 2400, "base_price": 4250.00},
            {"label": "4200 x 2400mm (3-panel)", "width": 4200, "height": 2400, "base_price": 5600.00},
            {"label": "6000 x 2700mm (4-panel)", "width": 6000, "height": 2700, "base_price": 8500.00},
        ],
        "image_placeholder": "sliding-door",
    },
    {
        "id": "bifold-door",
        "name": "Steel Bifold Door",
        "category": "doors",
        "description": "Multi-panel bifold door with steel frame. Opens your living space to the outdoors. Configurations from 2 to 7 panels with 90% clear opening.",
        "features": ["90% clear opening", "2 to 7 panel configs", "Heavy-duty track system", "Stacking left or right", "Powder-coated finish"],
        "sizes": [
            {"label": "1800 x 2100mm (2-panel)", "width": 1800, "height": 2100, "base_price": 3200.00},
            {"label": "2700 x 2100mm (3-panel)", "width": 2700, "height": 2100, "base_price": 4350.00},
            {"label": "3600 x 2400mm (4-panel)", "width": 3600, "height": 2400, "base_price": 5800.00},
            {"label": "4500 x 2400mm (5-panel)", "width": 4500, "height": 2400, "base_price": 7200.00},
            {"label": "5400 x 2700mm (6-panel)", "width": 5400, "height": 2700, "base_price": 9100.00},
        ],
        "image_placeholder": "bifold-door",
    },
    {
        "id": "pivot-door",
        "name": "Steel Pivot Door",
        "category": "doors",
        "description": "Architectural pivot door with concealed floor spring. A bold design statement for premium entries. Available in steel frame with glass or panel infill.",
        "features": ["Concealed floor spring", "Up to 1200mm wide", "Top and bottom pivot points", "Soft-close mechanism", "Custom steel patterns"],
        "sizes": [
            {"label": "900 x 2400mm", "width": 900, "height": 2400, "base_price": 3800.00},
            {"label": "1000 x 2400mm", "width": 1000, "height": 2400, "base_price": 4200.00},
            {"label": "1100 x 2700mm", "width": 1100, "height": 2700, "base_price": 4800.00},
            {"label": "1200 x 2700mm", "width": 1200, "height": 2700, "base_price": 5400.00},
            {"label": "1200 x 3000mm", "width": 1200, "height": 3000, "base_price": 6200.00},
        ],
        "image_placeholder": "pivot-door",
    },
]

GLASS_OPTIONS = [
    {"id": "clear-6mm", "name": "6mm Clear Float", "multiplier": 1.0},
    {"id": "laminated-6.38mm", "name": "6.38mm Clear Laminated", "multiplier": 1.0},
    {"id": "low-e", "name": "Low-E Performance Glass", "multiplier": 1.25},
    {"id": "double-glazed", "name": "Double Glazed IGU", "multiplier": 1.65},
    {"id": "double-glazed-low-e", "name": "Double Glazed Low-E IGU", "multiplier": 1.85},
    {"id": "acoustic", "name": "Acoustic Laminated (10.38mm)", "multiplier": 1.55},
    {"id": "tinted", "name": "Grey/Bronze Tinted", "multiplier": 1.15},
    {"id": "obscure", "name": "Obscure/Privacy Glass", "multiplier": 1.10},
]

FINISH_OPTIONS = [
    {"id": "matt-black", "name": "Matt Black", "surcharge": 0},
    {"id": "satin-black", "name": "Satin Black", "surcharge": 0},
    {"id": "monument", "name": "Monument (Colorbond)", "surcharge": 50},
    {"id": "woodland-grey", "name": "Woodland Grey (Colorbond)", "surcharge": 50},
    {"id": "surfmist", "name": "Surfmist (Colorbond)", "surcharge": 50},
    {"id": "custom-ral", "name": "Custom RAL Colour", "surcharge": 150},
    {"id": "natural-steel", "name": "Natural Steel (Clear Coat)", "surcharge": 85},
]

ADDON_OPTIONS = [
    {"id": "flyscreen", "name": "Fly Screen", "price": 185.00, "applies_to": ["windows"]},
    {"id": "security-mesh", "name": "Security Mesh Screen", "price": 350.00, "applies_to": ["windows", "doors"]},
    {"id": "hardware-upgrade", "name": "Premium Hardware Upgrade", "price": 220.00, "applies_to": ["doors"]},
    {"id": "sidelight", "name": "Fixed Sidelight Panel", "price": 480.00, "applies_to": ["doors"]},
    {"id": "transom", "name": "Transom Window Above", "price": 390.00, "applies_to": ["windows", "doors"]},
    {"id": "bal-rating", "name": "BAL-40 Bushfire Rating", "price": 275.00, "applies_to": ["windows", "doors"]},
]


def get_all_products():
    """Return all products (windows + doors)."""
    return WINDOW_TYPES + DOOR_TYPES


def get_product_by_id(product_id: str):
    """Look up a single product by its ID."""
    for product in get_all_products():
        if product["id"] == product_id:
            return product
    return None
