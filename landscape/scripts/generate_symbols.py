#!/usr/bin/env python3
"""
generate_symbols.py
Netrun Systems — Landscape CAD Symbol Generator
Generates 40 geometric DXF symbols for irrigation, hardscape, lighting, and site features.

Scale: 1:1  (1 drawing unit = 1 foot)
Format: DXF R2013 (LibreCAD compatible)
Output: ../symbols/generated/
"""

import math
import os
import ezdxf
from ezdxf import colors
from ezdxf.enums import TextEntityAlignment

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "symbols", "generated")
DXF_VERSION = "R2013"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def new_doc():
    """Return a fresh DXF document with layer 0 configured color-by-layer."""
    doc = ezdxf.new(dxfversion=DXF_VERSION)
    # Layer "0" already exists; set color to BYLAYER (256 = by layer)
    layer = doc.layers.get("0")
    layer.dxf.color = 7  # white/black — standard for layer 0
    return doc


def save(doc, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    doc.saveas(path)
    print(f"  wrote {filename}")


def add_text(msp, text, insert, height=0.5, layer="0"):
    msp.add_text(
        text,
        dxfattribs={
            "insert": insert,
            "height": height,
            "layer": layer,
            "halign": 1,  # center
            "valign": 2,  # middle
        },
    )


def add_centered_text(msp, text, x, y, height=0.5):
    """Add text centered on (x,y)."""
    t = msp.add_text(text, dxfattribs={"height": height, "layer": "0"})
    t.set_placement((x, y), align=TextEntityAlignment.MIDDLE_CENTER)


def filled_circle(msp, center, radius, layer="0"):
    """Approximate a filled circle with a solid hatch."""
    hatch = msp.add_hatch(color=256, dxfattribs={"layer": layer})
    hatch.set_pattern_fill("SOLID")
    edge_path = hatch.paths.add_edge_path()
    edge_path.add_arc(center=center, radius=radius, start_angle=0, end_angle=360)


def crosshatch_rect(msp, x0, y0, x1, y1, spacing=0.3, layer="0"):
    """Draw diagonal crosshatch lines inside a rectangle."""
    dx = x1 - x0
    dy = y1 - y0
    diag = dx + dy
    step = spacing
    t = -diag
    while t <= diag:
        # 45-degree lines (bottom-left to top-right)
        sx = x0 + t
        sy = y0
        ex = x0 + t + diag
        ey = y0 + diag
        # clip to rect
        pts = _clip_line_to_rect(sx, sy, ex, ey, x0, y0, x1, y1)
        if pts:
            msp.add_line(pts[0], pts[1], dxfattribs={"layer": layer})
        t += step


def _clip_line_to_rect(sx, sy, ex, ey, rx0, ry0, rx1, ry1):
    """Liang-Barsky line clipping; returns [(x0,y0),(x1,y1)] or None."""
    dx = ex - sx
    dy = ey - sy
    p = [-dx, dx, -dy, dy]
    q = [sx - rx0, rx1 - sx, sy - ry0, ry1 - sy]
    t0, t1 = 0.0, 1.0
    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return None
        elif pi < 0:
            t0 = max(t0, qi / pi)
        else:
            t1 = min(t1, qi / pi)
    if t0 > t1:
        return None
    return [(sx + t0 * dx, sy + t0 * dy), (sx + t1 * dx, sy + t1 * dy)]


def dashed_circle(msp, center, radius, segments=36, dash_frac=0.5, layer="0"):
    """Draw a dashed circle using alternating arc segments."""
    step = 360.0 / segments
    for i in range(segments):
        if i % 2 == 0:
            start_a = i * step
            end_a = start_a + step * dash_frac
            msp.add_arc(
                center=center,
                radius=radius,
                start_angle=start_a,
                end_angle=end_a,
                dxfattribs={"layer": layer},
            )


def grid_fill(msp, x0, y0, x1, y1, col_spacing=0.5, row_spacing=0.5, layer="0"):
    """Draw a grid of lines inside a rectangle."""
    x = x0 + col_spacing
    while x < x1:
        msp.add_line((x, y0), (x, y1), dxfattribs={"layer": layer})
        x += col_spacing
    y = y0 + row_spacing
    while y < y1:
        msp.add_line((x0, y), (x1, y), dxfattribs={"layer": layer})
        y += row_spacing


def dot_stipple(msp, x0, y0, x1, y1, cols, rows, radius=0.04, layer="0"):
    """Place small circles on a regular grid inside a rectangle."""
    col_step = (x1 - x0) / cols
    row_step = (y1 - y0) / rows
    for r in range(rows):
        for c in range(cols):
            cx = x0 + col_step * (c + 0.5)
            cy = y0 + row_step * (r + 0.5)
            msp.add_circle((cx, cy), radius, dxfattribs={"layer": layer})


def arrow_head(msp, tip, direction_deg, length=0.3, half_width=0.15, layer="0"):
    """Draw a filled arrowhead at `tip` pointing in `direction_deg`."""
    rad = math.radians(direction_deg)
    # base center
    bx = tip[0] - length * math.cos(rad)
    by = tip[1] - length * math.sin(rad)
    perp = math.radians(direction_deg + 90)
    lx = bx + half_width * math.cos(perp)
    ly = by + half_width * math.sin(perp)
    rx = bx - half_width * math.cos(perp)
    ry = by - half_width * math.sin(perp)
    msp.add_lwpolyline(
        [(lx, ly), tip, (rx, ry), (lx, ly)],
        dxfattribs={"layer": layer, "closed": True},
    )


# ---------------------------------------------------------------------------
# Irrigation symbols (1–9)
# ---------------------------------------------------------------------------

def gen_irrigation_drip_emitter():
    doc = new_doc()
    msp = doc.modelspace()
    filled_circle(msp, (0, 0), 0.25)
    msp.add_circle((0, 0), 0.25, dxfattribs={"layer": "0"})
    save(doc, "irrigation_drip_emitter.dxf")


def gen_irrigation_spray_quarter():
    doc = new_doc()
    msp = doc.modelspace()
    r = 5.0
    # 90-degree arc (0–90 degrees)
    msp.add_arc((0, 0), r, 0, 90, dxfattribs={"layer": "0"})
    # two radius lines
    msp.add_line((0, 0), (r, 0), dxfattribs={"layer": "0"})
    msp.add_line((0, 0), (0, r), dxfattribs={"layer": "0"})
    # center dot
    msp.add_circle((0, 0), 0.1, dxfattribs={"layer": "0"})
    save(doc, "irrigation_spray_quarter.dxf")


def gen_irrigation_spray_half():
    doc = new_doc()
    msp = doc.modelspace()
    r = 5.0
    msp.add_arc((0, 0), r, 0, 180, dxfattribs={"layer": "0"})
    msp.add_line((0, 0), (r, 0), dxfattribs={"layer": "0"})
    msp.add_line((0, 0), (-r, 0), dxfattribs={"layer": "0"})
    msp.add_circle((0, 0), 0.1, dxfattribs={"layer": "0"})
    save(doc, "irrigation_spray_half.dxf")


def gen_irrigation_spray_full():
    doc = new_doc()
    msp = doc.modelspace()
    r = 5.0
    dashed_circle(msp, (0, 0), r)
    msp.add_circle((0, 0), 0.15, dxfattribs={"layer": "0"})
    save(doc, "irrigation_spray_full.dxf")


def gen_irrigation_rotor():
    doc = new_doc()
    msp = doc.modelspace()
    r = 25.0
    # coverage arc (dashed, 180 degrees)
    dashed_circle(msp, (0, 0), r)
    # head symbol: small circle + radius line
    msp.add_circle((0, 0), 0.3, dxfattribs={"layer": "0"})
    msp.add_line((0, 0), (r, 0), dxfattribs={"layer": "0"})
    save(doc, "irrigation_rotor.dxf")


def gen_irrigation_bubbler():
    doc = new_doc()
    msp = doc.modelspace()
    r = 0.5
    msp.add_circle((0, 0), r, dxfattribs={"layer": "0"})
    filled_circle(msp, (0, 0), 0.08)
    msp.add_circle((0, 0), 0.08, dxfattribs={"layer": "0"})
    save(doc, "irrigation_bubbler.dxf")


def gen_irrigation_valve_box():
    doc = new_doc()
    msp = doc.modelspace()
    # 1x1 ft rectangle centered at origin
    msp.add_lwpolyline(
        [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    add_centered_text(msp, "V", 0, 0, height=0.5)
    save(doc, "irrigation_valve_box.dxf")


def gen_irrigation_backflow():
    doc = new_doc()
    msp = doc.modelspace()
    # 1x1.5 ft rectangle
    msp.add_lwpolyline(
        [(-0.5, -0.75), (0.5, -0.75), (0.5, 0.75), (-0.5, 0.75)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    # triangle arrow pointing right
    msp.add_lwpolyline(
        [(-0.25, -0.2), (0.25, 0), (-0.25, 0.2), (-0.25, -0.2)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    save(doc, "irrigation_backflow.dxf")


def gen_irrigation_controller():
    doc = new_doc()
    msp = doc.modelspace()
    # 0.5x0.5 ft rectangle
    msp.add_lwpolyline(
        [(-0.25, -0.25), (0.25, -0.25), (0.25, 0.25), (-0.25, 0.25)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    add_centered_text(msp, "C", 0, 0, height=0.25)
    save(doc, "irrigation_controller.dxf")


# ---------------------------------------------------------------------------
# Hardscape Structure Symbols (10–19)
# ---------------------------------------------------------------------------

def gen_hardscape_fire_pit():
    doc = new_doc()
    msp = doc.modelspace()
    outer_r = 2.0  # 4 ft dia
    inner_r = 1.3
    msp.add_circle((0, 0), outer_r, dxfattribs={"layer": "0"})
    msp.add_circle((0, 0), inner_r, dxfattribs={"layer": "0"})
    # flame-like tick marks radiating inward
    for angle_deg in range(0, 360, 45):
        rad = math.radians(angle_deg)
        x0 = inner_r * math.cos(rad)
        y0 = inner_r * math.sin(rad)
        x1 = (inner_r - 0.4) * math.cos(rad)
        y1 = (inner_r - 0.4) * math.sin(rad)
        msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": "0"})
    save(doc, "hardscape_fire_pit.dxf")


def gen_hardscape_raised_planter():
    doc = new_doc()
    msp = doc.modelspace()
    # 4x8 ft, centered
    msp.add_lwpolyline(
        [(-2, -4), (2, -4), (2, 4), (-2, 4)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    # inner offset (double-line border, 0.2 ft inset)
    o = 0.2
    msp.add_lwpolyline(
        [(-2 + o, -4 + o), (2 - o, -4 + o), (2 - o, 4 - o), (-2 + o, 4 - o)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    save(doc, "hardscape_raised_planter.dxf")


def gen_hardscape_seat_wall():
    doc = new_doc()
    msp = doc.modelspace()
    # 1.5 wide x 8 long
    msp.add_lwpolyline(
        [(-0.75, -4), (0.75, -4), (0.75, 4), (-0.75, 4)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    crosshatch_rect(msp, -0.75, -4, 0.75, 4, spacing=0.5)
    save(doc, "hardscape_seat_wall.dxf")


def gen_hardscape_pergola():
    doc = new_doc()
    msp = doc.modelspace()
    # 10x12 ft dashed rectangle
    pts = [(-5, -6), (5, -6), (5, 6), (-5, 6), (-5, -6)]
    dash_len = 0.6
    gap_len = 0.3
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        length = math.hypot(x1 - x0, y1 - y0)
        dx = (x1 - x0) / length
        dy = (y1 - y0) / length
        t = 0
        drawing = True
        while t < length:
            seg = dash_len if drawing else gap_len
            t2 = min(t + seg, length)
            if drawing:
                msp.add_line(
                    (x0 + t * dx, y0 + t * dy),
                    (x0 + t2 * dx, y0 + t2 * dy),
                    dxfattribs={"layer": "0"},
                )
            t = t2
            drawing = not drawing
    # corner post dots
    for cx, cy in [(-5, -6), (5, -6), (5, 6), (-5, 6)]:
        filled_circle(msp, (cx, cy), 0.2)
        msp.add_circle((cx, cy), 0.2, dxfattribs={"layer": "0"})
    save(doc, "hardscape_pergola.dxf")


def gen_hardscape_water_feature():
    doc = new_doc()
    msp = doc.modelspace()
    # outer circle 3 ft radius
    for r in [1.5, 1.0, 0.6, 0.3]:
        msp.add_circle((0, 0), r, dxfattribs={"layer": "0"})
    save(doc, "hardscape_water_feature.dxf")


def gen_hardscape_spa():
    doc = new_doc()
    msp = doc.modelspace()
    r = 3.5  # 7 ft dia
    msp.add_circle((0, 0), r, dxfattribs={"layer": "0"})
    msp.add_circle((0, 0), r - 0.25, dxfattribs={"layer": "0"})
    add_centered_text(msp, "SPA", 0, 0, height=0.6)
    save(doc, "hardscape_spa.dxf")


def gen_hardscape_outdoor_kitchen():
    doc = new_doc()
    msp = doc.modelspace()
    # L-shape: main run 8x2, side wing 3x2
    # Main counter (horizontal)
    msp.add_lwpolyline(
        [(0, 0), (8, 0), (8, 2), (0, 2), (0, 0)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    # Side wing (vertical, attached at left)
    msp.add_lwpolyline(
        [(0, 2), (3, 2), (3, 5), (0, 5), (0, 2)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    # counter line (inner ledge line at 0.5 ft from front)
    msp.add_line((0, 0.5), (8, 0.5), dxfattribs={"layer": "0"})
    msp.add_line((0, 2.5), (3, 2.5), dxfattribs={"layer": "0"})
    save(doc, "hardscape_outdoor_kitchen.dxf")


def gen_hardscape_retaining_wall():
    doc = new_doc()
    msp = doc.modelspace()
    # thick wall section: 1 ft thick x 8 ft long
    msp.add_lwpolyline(
        [(0, 0), (8, 0), (8, 1), (0, 1)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    crosshatch_rect(msp, 0, 0, 8, 1, spacing=0.4)
    save(doc, "hardscape_retaining_wall.dxf")


def gen_hardscape_gabion_wall():
    doc = new_doc()
    msp = doc.modelspace()
    # 8 ft long x 2 ft tall section
    msp.add_lwpolyline(
        [(0, 0), (8, 0), (8, 2), (0, 2)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    grid_fill(msp, 0, 0, 8, 2, col_spacing=1.0, row_spacing=0.5)
    save(doc, "hardscape_gabion_wall.dxf")


def gen_hardscape_stepping_stones():
    doc = new_doc()
    msp = doc.modelspace()
    # 3 circles, 1.5 ft radius, spaced 2 ft apart (center to center = 2+1.5*2=5? — use 2 ft between edges = 5 ft c-to-c)
    spacing = 5.0  # center-to-center (1.5 dia + 2 ft gap)
    r = 0.75
    for i in range(3):
        cx = i * spacing
        msp.add_circle((cx, 0), r, dxfattribs={"layer": "0"})
    save(doc, "hardscape_stepping_stones.dxf")


# ---------------------------------------------------------------------------
# Lighting Symbols (20–23)
# ---------------------------------------------------------------------------

def gen_lighting_path_light():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_circle((0, 0), 0.5, dxfattribs={"layer": "0"})
    # 4 ray lines at 45-degree intervals
    ray_len = 0.8
    for angle_deg in [0, 90, 180, 270]:
        rad = math.radians(angle_deg)
        x1 = (0.5 + ray_len) * math.cos(rad)
        y1 = (0.5 + ray_len) * math.sin(rad)
        x0 = 0.5 * math.cos(rad)
        y0 = 0.5 * math.sin(rad)
        msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": "0"})
    save(doc, "lighting_path_light.dxf")


def gen_lighting_spot_uplight():
    doc = new_doc()
    msp = doc.modelspace()
    # isoceles triangle pointing up, 0.5 ft half-base
    msp.add_lwpolyline(
        [(-0.25, 0), (0.25, 0), (0, 0.5), (-0.25, 0)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    # upward ray lines
    msp.add_line((0, 0.5), (-0.3, 1.1), dxfattribs={"layer": "0"})
    msp.add_line((0, 0.5), (0, 1.1), dxfattribs={"layer": "0"})
    msp.add_line((0, 0.5), (0.3, 1.1), dxfattribs={"layer": "0"})
    save(doc, "lighting_spot_uplight.dxf")


def gen_lighting_wall_sconce():
    doc = new_doc()
    msp = doc.modelspace()
    # wall line (horizontal)
    msp.add_line((-1.0, 0), (1.0, 0), dxfattribs={"layer": "0"})
    # half-circle protruding below wall (semi-circle, 0.5 ft radius)
    msp.add_arc((0, 0), 0.5, 180, 360, dxfattribs={"layer": "0"})
    msp.add_line((-0.5, 0), (0.5, 0), dxfattribs={"layer": "0"})
    # ray lines below
    for angle_deg in [210, 270, 330]:
        rad = math.radians(angle_deg)
        x0 = 0.5 * math.cos(rad)
        y0 = 0.5 * math.sin(rad)
        x1 = 0.9 * math.cos(rad)
        y1 = 0.9 * math.sin(rad)
        msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": "0"})
    save(doc, "lighting_wall_sconce.dxf")


def gen_lighting_string_lights():
    doc = new_doc()
    msp = doc.modelspace()
    total_len = 10.0
    bulb_spacing = 1.5
    dash_len = 0.5
    gap_len = 0.3
    # dashed line
    t = 0
    drawing = True
    while t < total_len:
        seg = dash_len if drawing else gap_len
        t2 = min(t + seg, total_len)
        if drawing:
            msp.add_line((t, 0), (t2, 0), dxfattribs={"layer": "0"})
        t = t2
        drawing = not drawing
    # small circles along line
    pos = bulb_spacing
    while pos < total_len:
        msp.add_circle((pos, 0), 0.12, dxfattribs={"layer": "0"})
        pos += bulb_spacing
    save(doc, "lighting_string_lights.dxf")


# ---------------------------------------------------------------------------
# Edge/Border Symbols (24–27)
# ---------------------------------------------------------------------------

def gen_edge_steel():
    doc = new_doc()
    msp = doc.modelspace()
    # thin line with perpendicular tick marks
    msp.add_line((0, 0), (8, 0), dxfattribs={"layer": "0"})
    for x in range(1, 8):
        msp.add_line((x, -0.15), (x, 0.15), dxfattribs={"layer": "0"})
    save(doc, "edge_steel.dxf")


def gen_edge_stone():
    doc = new_doc()
    msp = doc.modelspace()
    # irregular thick line — series of short angled segments
    pts = [
        (0, 0), (1.0, 0.15), (2.1, -0.1), (3.0, 0.2),
        (4.2, 0.05), (5.1, -0.15), (6.0, 0.1), (7.0, -0.05), (8.0, 0),
    ]
    for i in range(len(pts) - 1):
        msp.add_line(pts[i], pts[i + 1], dxfattribs={"layer": "0"})
    # second slightly offset line for thickness
    pts2 = [
        (0, 0.25), (1.0, 0.4), (2.1, 0.15), (3.0, 0.45),
        (4.2, 0.3), (5.1, 0.1), (6.0, 0.35), (7.0, 0.2), (8.0, 0.25),
    ]
    for i in range(len(pts2) - 1):
        msp.add_line(pts2[i], pts2[i + 1], dxfattribs={"layer": "0"})
    save(doc, "edge_stone.dxf")


def gen_edge_mow_strip():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_line((0, 0), (8, 0), dxfattribs={"layer": "0"})
    msp.add_line((0, 0.5), (8, 0.5), dxfattribs={"layer": "0"})
    save(doc, "edge_mow_strip.dxf")


def gen_edge_boulder_border():
    doc = new_doc()
    msp = doc.modelspace()
    # 3 irregular circles in a cluster
    stones = [
        (0, 0, 0.9),
        (1.4, 0.2, 0.7),
        (0.6, -1.1, 0.6),
    ]
    for cx, cy, r in stones:
        # approximate irregular shape with a slightly faceted polygon
        pts = []
        n = 10
        for k in range(n):
            angle = 2 * math.pi * k / n
            # slight irregularity: vary radius by up to 15%
            jitter = 1.0 + 0.15 * math.sin(3 * angle + cx)
            pts.append((cx + r * jitter * math.cos(angle), cy + r * jitter * math.sin(angle)))
        msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": "0"})
    save(doc, "edge_boulder_border.dxf")


# ---------------------------------------------------------------------------
# Site Feature Symbols (28–33)
# ---------------------------------------------------------------------------

def gen_site_utility_box():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline(
        [(-1.5, -1.5), (1.5, -1.5), (1.5, 1.5), (-1.5, 1.5)],
        close=True,
        dxfattribs={"layer": "0"},
    )
    # diagonal lines
    msp.add_line((-1.5, -1.5), (1.5, 1.5), dxfattribs={"layer": "0"})
    msp.add_line((1.5, -1.5), (-1.5, 1.5), dxfattribs={"layer": "0"})
    add_centered_text(msp, "UTIL", 0, 0, height=0.4)
    save(doc, "site_utility_box.dxf")


def gen_site_drainage_arrow():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_line((0, 0), (6, 0), dxfattribs={"layer": "0"})
    arrow_head(msp, (6, 0), 0, length=0.4, half_width=0.2)
    add_centered_text(msp, "DRAIN", 3, 0.4, height=0.4)
    save(doc, "site_drainage_arrow.dxf")


def gen_site_existing_fence():
    doc = new_doc()
    msp = doc.modelspace()
    total = 10.0
    # dashed line
    t = 0
    drawing = True
    dash, gap = 0.6, 0.3
    while t < total:
        seg = dash if drawing else gap
        t2 = min(t + seg, total)
        if drawing:
            msp.add_line((t, 0), (t2, 0), dxfattribs={"layer": "0"})
        t = t2
        drawing = not drawing
    # "F" labels at intervals
    for pos in [1.5, 4.5, 7.5]:
        add_centered_text(msp, "F", pos, 0.35, height=0.35)
    save(doc, "site_existing_fence.dxf")


def gen_site_contour_line():
    doc = new_doc()
    msp = doc.modelspace()
    # thin curved-ish line (approximated by a polyline)
    pts = [(0, 0), (2, 0.2), (4, -0.1), (6, 0.15), (8, 0)]
    for i in range(len(pts) - 1):
        msp.add_line(pts[i], pts[i + 1], dxfattribs={"layer": "0"})
    add_centered_text(msp, "100.0", 4, 0.5, height=0.4)
    save(doc, "site_contour_line.dxf")


def gen_site_boulder_large():
    doc = new_doc()
    msp = doc.modelspace()
    r = 2.5
    n = 14
    pts = []
    for k in range(n):
        angle = 2 * math.pi * k / n
        jitter = 1.0 + 0.2 * math.sin(2.5 * angle) + 0.1 * math.cos(5 * angle)
        pts.append((r * jitter * math.cos(angle), r * jitter * math.sin(angle)))
    msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": "0"})
    # inner stipple lines
    for angle_deg in range(20, 160, 30):
        rad = math.radians(angle_deg)
        x0 = 0.5 * math.cos(rad)
        y0 = 0.5 * math.sin(rad)
        x1 = 1.5 * math.cos(rad)
        y1 = 1.5 * math.sin(rad)
        msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": "0"})
    save(doc, "site_boulder_large.dxf")


def gen_site_rock_outcrop():
    doc = new_doc()
    msp = doc.modelspace()
    rocks = [
        (0, 0, 1.5, 12),
        (2.5, 0.5, 1.0, 10),
        (-1.8, 1.0, 0.9, 9),
        (1.0, -1.5, 0.8, 9),
        (-0.5, -1.8, 0.7, 8),
        (3.0, -0.8, 0.6, 8),
        (-2.5, -0.5, 0.7, 8),
    ]
    for cx, cy, r, n in rocks:
        pts = []
        for k in range(n):
            angle = 2 * math.pi * k / n
            jitter = 1.0 + 0.18 * math.sin(3 * angle + cx * 0.5)
            pts.append((cx + r * jitter * math.cos(angle), cy + r * jitter * math.sin(angle)))
        msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": "0"})
    save(doc, "site_rock_outcrop.dxf")


# ---------------------------------------------------------------------------
# Hardscape Fill Pattern Samples (34–40)
# ---------------------------------------------------------------------------

def gen_fill_decomposed_granite():
    doc = new_doc()
    msp = doc.modelspace()
    # 4x4 ft border
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    dot_stipple(msp, 0.1, 0.1, 3.9, 3.9, cols=20, rows=20, radius=0.04)
    save(doc, "fill_decomposed_granite.dxf")


def gen_fill_flagstone():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    # irregular flagstone joint pattern — a grid with slight offsets
    slabs = [
        [(0, 0), (1.8, 0), (1.8, 1.2), (0, 1.2)],
        [(1.9, 0), (4, 0), (4, 1.0), (1.9, 1.0)],
        [(0, 1.3), (1.2, 1.3), (1.2, 2.5), (0, 2.5)],
        [(1.3, 1.1), (4, 1.1), (4, 2.3), (1.3, 2.3)],
        [(0, 2.6), (2.2, 2.6), (2.2, 4.0), (0, 4.0)],
        [(2.3, 2.4), (4, 2.4), (4, 4), (2.3, 4)],
    ]
    for pts in slabs:
        msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": "0"})
    save(doc, "fill_flagstone.dxf")


def gen_fill_permeable_pavers():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    # regular brick grid 0.5 x 0.25 ft pavers
    pw, ph = 0.5, 0.25
    row = 0
    y = 0
    while y < 4:
        offset = (pw / 2) if (row % 2 == 1) else 0
        x = -offset
        while x < 4:
            x0, y0 = max(x, 0), y
            x1, y1 = min(x + pw, 4), min(y + ph, 4)
            if x1 > x0 and y1 > y0:
                msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], close=True, dxfattribs={"layer": "0"})
            x += pw
        y += ph
        row += 1
    save(doc, "fill_permeable_pavers.dxf")


def gen_fill_gravel():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    # random-looking circles (deterministic using sine)
    import hashlib
    positions = []
    for i in range(60):
        h = int(hashlib.md5(str(i).encode()).hexdigest()[:8], 16)
        x = 0.2 + (h % 1000) / 1000.0 * 3.6
        y = 0.2 + ((h // 1000) % 1000) / 1000.0 * 3.6
        r = 0.06 + (h % 5) * 0.01
        positions.append((x, y, r))
    for x, y, r in positions:
        msp.add_circle((x, y), r, dxfattribs={"layer": "0"})
    save(doc, "fill_gravel.dxf")


def gen_fill_brick_herringbone():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    # herringbone pattern: 45-degree rotated bricks 0.5 x 0.25 ft
    bw, bh = 0.5, 0.25
    # generate pairs of bricks in L-units rotated 45 degrees
    # Simplified: alternating horizontal and vertical bricks in a diagonal grid
    step = bw  # 0.5 ft diagonal step
    for row in range(-8, 16):
        for col in range(-2, 12):
            ox = (col + row * 0.5) * bw
            oy = row * bw
            if row % 2 == 0:
                # horizontal brick
                pts = [(ox, oy), (ox + bw, oy), (ox + bw, oy + bh), (ox, oy + bh)]
            else:
                # vertical brick
                pts = [(ox, oy), (ox + bh, oy), (ox + bh, oy + bw), (ox, oy + bw)]
            # clip to 4x4 box
            clipped = [(max(0, min(4, x)), max(0, min(4, y))) for x, y in pts]
            xs = [p[0] for p in clipped]
            ys = [p[1] for p in clipped]
            if max(xs) > min(xs) and max(ys) > min(ys):
                if any(0 <= x <= 4 and 0 <= y <= 4 for x, y in zip(xs, ys)):
                    msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": "0"})
    save(doc, "fill_brick_herringbone.dxf")


def gen_fill_concrete():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    # light stipple — sparse dot pattern
    dot_stipple(msp, 0.2, 0.2, 3.8, 3.8, cols=10, rows=10, radius=0.03)
    # control joint lines
    msp.add_line((2, 0), (2, 4), dxfattribs={"layer": "0"})
    msp.add_line((0, 2), (4, 2), dxfattribs={"layer": "0"})
    save(doc, "fill_concrete.dxf")


def gen_fill_dry_creek():
    doc = new_doc()
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (4, 0), (4, 4), (0, 4)], close=True, dxfattribs={"layer": "0"})
    # rounded rock pattern — circles of varying size
    rock_data = [
        (0.4, 0.4, 0.25), (1.1, 0.3, 0.18), (0.7, 0.9, 0.22),
        (1.6, 0.7, 0.3),  (2.2, 0.4, 0.2),  (2.8, 0.6, 0.25),
        (3.4, 0.3, 0.18), (3.7, 0.9, 0.22), (0.3, 1.5, 0.2),
        (0.9, 1.8, 0.28), (1.5, 1.4, 0.22), (2.1, 1.7, 0.18),
        (2.6, 1.3, 0.3),  (3.2, 1.6, 0.22), (3.7, 1.4, 0.19),
        (0.5, 2.4, 0.25), (1.1, 2.2, 0.18), (1.7, 2.6, 0.22),
        (2.3, 2.3, 0.28), (2.9, 2.5, 0.2),  (3.5, 2.2, 0.24),
        (0.4, 3.2, 0.2),  (1.0, 3.5, 0.25), (1.7, 3.1, 0.18),
        (2.3, 3.4, 0.22), (2.9, 3.2, 0.28), (3.5, 3.5, 0.2),
    ]
    for cx, cy, r in rock_data:
        msp.add_circle((cx, cy), r, dxfattribs={"layer": "0"})
    save(doc, "fill_dry_creek.dxf")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating 40 DXF symbols → {os.path.abspath(OUTPUT_DIR)}\n")

    generators = [
        # Irrigation (1–9)
        gen_irrigation_drip_emitter,
        gen_irrigation_spray_quarter,
        gen_irrigation_spray_half,
        gen_irrigation_spray_full,
        gen_irrigation_rotor,
        gen_irrigation_bubbler,
        gen_irrigation_valve_box,
        gen_irrigation_backflow,
        gen_irrigation_controller,
        # Hardscape (10–19)
        gen_hardscape_fire_pit,
        gen_hardscape_raised_planter,
        gen_hardscape_seat_wall,
        gen_hardscape_pergola,
        gen_hardscape_water_feature,
        gen_hardscape_spa,
        gen_hardscape_outdoor_kitchen,
        gen_hardscape_retaining_wall,
        gen_hardscape_gabion_wall,
        gen_hardscape_stepping_stones,
        # Lighting (20–23)
        gen_lighting_path_light,
        gen_lighting_spot_uplight,
        gen_lighting_wall_sconce,
        gen_lighting_string_lights,
        # Edge/Border (24–27)
        gen_edge_steel,
        gen_edge_stone,
        gen_edge_mow_strip,
        gen_edge_boulder_border,
        # Site Features (28–33)
        gen_site_utility_box,
        gen_site_drainage_arrow,
        gen_site_existing_fence,
        gen_site_contour_line,
        gen_site_boulder_large,
        gen_site_rock_outcrop,
        # Fill Patterns (34–40)
        gen_fill_decomposed_granite,
        gen_fill_flagstone,
        gen_fill_permeable_pavers,
        gen_fill_gravel,
        gen_fill_brick_herringbone,
        gen_fill_concrete,
        gen_fill_dry_creek,
    ]

    for i, gen_fn in enumerate(generators, start=1):
        print(f"[{i:02d}/40]", end=" ")
        gen_fn()

    print(f"\nDone. {len(generators)} files written to {os.path.abspath(OUTPUT_DIR)}")


if __name__ == "__main__":
    main()
