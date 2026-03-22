# Netrun CAD — Landscape Design Edition

A fork of [LibreCAD](https://github.com/LibreCAD/LibreCAD) customized for landscape architecture.

> **Primary tool**: The web app at **[cad.netrunsystems.com](https://cad.netrunsystems.com)** is now the primary design tool for most landscape work. It runs in the browser (iPad, desktop, any device), has Apple Pencil support, satellite basemap, KIRI scan import, Google Drive save, and full DXF/PDF export. The desktop app is best for production DXF/DWG work requiring complex editing or large file compatibility.

---

## Quick Start

### macOS
```bash
brew install cmake qt@6 boost freetype
mkdir build && cd build
cmake .. -DCMAKE_PREFIX_PATH=$(brew --prefix qt@6)
make -j$(sysctl -n hw.ncpu)
./desktop/LibreCAD
```

### Ubuntu/Debian
```bash
sudo apt install cmake qt6-base-dev libboost-all-dev libfreetype-dev libmuparser-dev
mkdir build && cd build
cmake ..
make -j$(nproc)
./desktop/LibreCAD
```

---

## AutoCAD LT Keybindings

Copy `landscape/autocad_aliases.txt` to your LibreCAD support directory:
- macOS: `~/Library/Application Support/LibreCAD/librecad.alias`
- Linux: `~/.local/share/LibreCAD/librecad.alias`
- Windows: `%APPDATA%\LibreCAD\librecad.alias`

All standard AutoCAD LT shortcuts work: L=Line, C=Circle, M=Move, TR=Trim, O=Offset, etc.

The web app also has all 88 AutoCAD LT shortcuts — type in the command line at the bottom of the screen or just press any letter key (the command line opens automatically, AutoCAD-style).

---

## Feature Comparison: Web App vs Desktop

| Feature | Web App (cad.netrunsystems.com) | Desktop App |
|---------|--------------------------------|-------------|
| Apple Pencil support | Yes (pressure-sensitive) | No |
| AutoCAD shortcuts | Yes (88 aliases + command line) | Yes (librecad.alias) |
| DXF import | Yes (LINE, LWPOLYLINE, CIRCLE, ARC, TEXT) | Full DXF/DWG support |
| DXF export | Yes (DXF R12) | Full DXF/DWG |
| PDF export | Yes (scale + title block) | Yes |
| Satellite basemap | Yes (Esri World Imagery) | No |
| KIRI 3D scan import | Yes (OBJ, PLY) | Planned |
| GeoJSON / KML import | Yes | No |
| Plant database | Yes (with symbol placement) | Planned |
| Google Drive save | Yes | No |
| Freehand drawing | Yes (Draw + Color modes) | No |
| Watercolor brushes | Yes | No |
| iPad / mobile | Yes | No |
| Offline use | Partial (localStorage) | Yes |

---

## Landscape Plugins (Desktop App)

| Plugin | Status | Description |
|--------|--------|-------------|
| AutoCAD Keybindings | Ready | Command aliases matching AutoCAD LT 2014 |
| GIS Import | Implemented in web app | GeoJSON, KML import (web); GeoTIFF/Shapefile planned for desktop |
| KIRI Scan Import | Implemented in web app | OBJ/PLY 3D scan → 2D plan view (web); desktop support planned |
| Plant Database | Implemented in web app | Searchable catalog with symbols (web); desktop plugin planned |
| Irrigation Planning | Planned | Sprinkler/drip layout with coverage visualization |

---

## Typical Landscape Design Workflow

1. **Site Survey**: Import GIS data or KIRI Engine scan in the web app, or import GeoTIFF/Shapefiles in the desktop
2. **Base Plan**: Draw hardscape — paths, walls, structures, fences (web app or desktop)
3. **Planting Plan**: Place plant symbols from the database on a planting layer (web app)
4. **Hand-color**: Switch to Color Mode on the iPad for watercolor washes (web app)
5. **Add Labels**: Text Mode for plant labels and annotations (web app)
6. **Export**: PDF at 1/4"=1' for client delivery, or DXF for contractors

---

## Layer Convention for Landscape Plans

| Layer | Color | Description |
|-------|-------|-------------|
| SITE-BOUNDARY | White | Property lines, setbacks |
| HARDSCAPE | Gray | Paths, patios, walls, structures |
| EXISTING-TREES | Green | Trees to preserve |
| PLANTING-TREES | Dark Green | New tree locations |
| PLANTING-SHRUBS | Light Green | Shrub beds |
| PLANTING-GROUND | Yellow-Green | Groundcover areas |
| IRRIGATION-MAIN | Blue | Main irrigation lines |
| IRRIGATION-DRIP | Cyan | Drip zones |
| IRRIGATION-SPRAY | Light Blue | Spray heads |
| DIMENSIONS | Red | Dimensions and notes |
| TEXT | White | Labels and annotations |

---

## Repository Structure

```
/data/workspace/github/
├── netrun-cad/           ← THIS REPO (desktop app, LibreCAD fork)
│   ├── ALLIE_GETTING_STARTED.md
│   ├── landscape/        ← Landscape-specific plugins and data
│   └── librecad/         ← LibreCAD source (GPLv2 upstream)
└── netrun-cad-web/       ← Web app (React/TypeScript, MIT)
    └── src/              ← Vite + React SPA
```

---

## License

- **Desktop app**: GPLv2 (inherited from LibreCAD)
- **Web app**: MIT
