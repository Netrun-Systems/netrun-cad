# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Netrun CAD** — a fork of LibreCAD customized for landscape design. Built for Allie Garza's landscape architecture practice.

**Upstream**: [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD) (GPLv2)
**Fork**: [Netrun-Systems/netrun-cad](https://github.com/Netrun-Systems/netrun-cad)
**Branch**: `landscape-design` (customizations), `master` (upstream sync)

## Target User

Allie Garza — landscape designer returning to practice after years using AutoCAD LT 2014.
- Creates 2D floor plans and planting plans for outdoor spaces
- Familiar with AutoCAD LT interface (command line, toolbars, layers, snaps)
- Needs DWG/DXF file compatibility for client deliverables
- Works on macOS

## Build Commands

```bash
# Dependencies (macOS)
brew install cmake qt@6 boost freetype

# Build
mkdir build && cd build
cmake .. -DCMAKE_PREFIX_PATH=$(brew --prefix qt@6)
make -j$(nproc)

# Run
./desktop/LibreCAD

# Dependencies (Ubuntu/Debian)
sudo apt install cmake qt6-base-dev libboost-all-dev libfreetype-dev

# Build
mkdir build && cd build
cmake ..
make -j$(nproc)
```

## Architecture

```
librecad/
├── src/
│   ├── actions/     # Drawing actions (line, circle, trim, etc.)
│   ├── cmd/         # Command line processor
│   ├── lib/         # Core geometry, math, DXF/DWG parsing
│   ├── main/        # Application entry, main window, MDI
│   ├── plugins/     # Plugin system (C++ shared libraries)
│   └── test/        # Unit tests
├── plugins/         # Built-in plugins directory
└── desktop/         # Desktop integration files
```

## Custom Landscape Design Features (Netrun additions)

All customizations are in the `plugins/` directory as separate plugins:

### 1. AutoCAD Keybindings (`plugins/autocad_compat/`)
- Maps AutoCAD LT keyboard shortcuts: L=Line, C=Circle, M=Move, TR=Trim, O=Offset, etc.
- Custom toolbar layout matching AutoCAD LT 2014

### 2. GIS Import (`plugins/gis_import/`)
- Import GeoTIFF, Shapefiles (.shp), KML/KMZ
- Uses GDAL/OGR library
- Converts GIS features to LibreCAD entities on appropriate layers

### 3. KIRI Engine Scan Import (`plugins/kiri_import/`)
- Import OBJ/PLY point cloud files from KIRI Engine iOS app
- Project 3D scan to 2D plan view
- Auto-generate site boundary from point cloud

### 4. Plant Database (`plugins/plant_database/`)
- SQLite-backed searchable plant catalog
- Plant symbols as LibreCAD blocks
- Zone info, water requirements, spacing data
- Planting schedule generation

### 5. Irrigation Planning (`plugins/irrigation/`)
- Sprinkler/drip head placement tools
- Coverage circle visualization
- GPM calculations and zone grouping

## Key Files

| File | Purpose |
|------|---------|
| `CMakeLists.txt` | Main build configuration |
| `librecad/src/cmd/rs_commands.cpp` | Command aliases (AutoCAD mapping goes here) |
| `librecad/src/main/qc_applicationwindow.cpp` | Main window, toolbar setup |
| `librecad/src/plugins/` | Plugin loading infrastructure |
| `librecad/src/lib/engine/rs_layer.cpp` | Layer management |
| `librecad/src/lib/fileio/` | DXF/DWG file I/O |

## Development Notes

- Keep all Netrun customizations in plugins/ or clearly marked sections to simplify upstream merging
- Use the `landscape-design` branch for all changes
- Sync upstream periodically: `git fetch upstream && git merge upstream/master`
- Test DWG/DXF import/export after any changes to file I/O
- The command line processor in `src/cmd/` is the closest match to AutoCAD's command interface
