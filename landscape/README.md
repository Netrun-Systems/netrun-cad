# Netrun CAD — Landscape Design Edition

A fork of [LibreCAD](https://github.com/LibreCAD/LibreCAD) customized for landscape architecture.

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

## AutoCAD LT Keybindings

Copy `landscape/autocad_aliases.txt` to your LibreCAD support directory:
- macOS: `~/Library/Application Support/LibreCAD/librecad.alias`
- Linux: `~/.local/share/LibreCAD/librecad.alias`
- Windows: `%APPDATA%\LibreCAD\librecad.alias`

All standard AutoCAD LT shortcuts work: L=Line, C=Circle, M=Move, TR=Trim, O=Offset, etc.

## Landscape Features (Plugins)

| Plugin | Status | Description |
|--------|--------|-------------|
| AutoCAD Keybindings | Ready | Command aliases matching AutoCAD LT 2014 |
| GIS Import | Planned | Import GeoTIFF, Shapefiles, KML/KMZ via GDAL |
| KIRI Scan Import | Planned | Import 3D scans from KIRI Engine, project to 2D |
| Plant Database | Planned | Searchable plant catalog with symbols and zone data |
| Irrigation Planning | Planned | Sprinkler/drip layout with coverage visualization |

## Typical Landscape Design Workflow

1. **Site Survey**: Import GIS data (property boundaries, topo) or KIRI Engine scan
2. **Base Plan**: Draw hardscape — paths, walls, structures, fences
3. **Planting Plan**: Place plant symbols from the database on a planting layer
4. **Irrigation**: Layout sprinkler heads and drip zones
5. **Export**: Save as DXF for client delivery or DWG via ODA converter

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

## License

GPLv2 (inherited from LibreCAD)
