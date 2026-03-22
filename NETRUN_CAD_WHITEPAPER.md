# Netrun CAD: An Open-Source Landscape Design Platform with Touch-First Drawing and Environmental Intelligence

**Netrun Systems** | March 2026
**Version**: 1.0
**Authors**: Daniel Garza, Founder & CEO; Allie Garza, Landscape Designer & Product Visionary

---

## 1. Executive Summary

Netrun CAD is an open-source landscape design platform built for the way designers actually work: with a pencil in one hand and a plan in the other.

The platform consists of two complementary products:

- **Netrun CAD Desktop** — a fork of LibreCAD (GPLv2), a full-featured 2D CAD application customized for landscape architecture. It provides AutoCAD LT command compatibility, DWG/DXF file support, and a plugin architecture for landscape-specific tools including GIS import, 3D scan integration, plant databases, and irrigation planning.

- **Netrun CAD Web** — a React/TypeScript web application with an HTML5 Canvas drawing engine designed for Apple Pencil on iPad. It offers four drawing modes (CAD, Draw, Color, Text) that allow designers to measure, draft, sketch, hand-color, and label plans entirely on screen — eliminating the print-draw-scan cycle that defines most landscape design workflows today.

Both products share a curated plant database of 59 species for USDA Zone 9b (Ojai Valley / Southern California) with WUCOLS water use ratings, drought tolerance scoring, and California native classification. A DXF symbol library of 45 plan-view symbols covers trees, shrubs, hardscape, irrigation, and lighting elements, with 84 additional landscape elements documented and mapped for future generation.

Netrun CAD targets residential landscape designers, small firms, and independent practitioners — professionals who need CAD precision without the cost of AutoCAD LT ($475/year) and artistic expression without the friction of analog workflows. The platform is built in California, for California landscapes, by a designer who draws every day.

---

## 2. The Problem

### The Cost Barrier

AutoCAD LT, the industry standard for 2D drafting, costs $475 per year. For an independent landscape designer returning to practice — or a small firm with two or three drafters — this is a significant annual expense with no ownership and no alternative. LibreCAD is free and open source but lacks landscape-specific tools, plant databases, and the touch-first design experience that modern tablets enable.

### The Analog Gap

Landscape design is an inherently artistic discipline. Designers draft hardscape layouts with CAD precision, but planting plans require organic, hand-drawn representation — species-specific canopy shapes, naturalistic groupings, watercolor washes that communicate material palettes to clients. No existing CAD tool bridges this gap.

The standard workflow today:

1. Draft base plan in AutoCAD LT (desktop, mouse and keyboard)
2. Print the plan on large-format paper (24x36 or larger)
3. Hand-draw planting symbols, annotations, and color washes with markers and pencils
4. Scan or photograph the colored plan back into digital format
5. Deliver to client as PDF or print

This print-draw-scan cycle wastes time, materials, and resolution. Every revision requires reprinting and redrawing. The designer's artistic work exists only on paper — fragile, non-editable, and disconnected from the digital drawing data.

### The Intelligence Gap

No landscape CAD tool includes built-in California native plant intelligence. Designers maintain personal spreadsheets of preferred species, manually cross-reference WUCOLS water use classifications for permit compliance, and lack integrated data on drought tolerance, fire resistance, and deer resistance. This knowledge exists in scattered government databases (WUCOLS V, USDA PLANTS, Calscape) but has never been consolidated into a design tool.

### The Data Gap

KIRI Engine and similar iOS apps can produce detailed 3D scans of existing sites — mature trees, boulder formations, grade changes — but there is no pathway from a 3D point cloud into a landscape CAD workflow. Similarly, GIS data (aerial imagery, property boundaries, topographic contours) requires separate expensive tools to access and integrate into design drawings.

---

## 3. Architecture

### Netrun CAD Desktop

**Status**: Implemented (build system, AutoCAD compatibility); Planned (landscape plugins)

Netrun CAD Desktop is a fork of [LibreCAD](https://github.com/LibreCAD/LibreCAD), a mature open-source 2D CAD application with over a decade of development history and thousands of active users.

**Core Stack**:
- Language: C++17
- UI Framework: Qt6
- Build System: CMake
- License: GPLv2 (inherited from LibreCAD)
- Platforms: Windows, macOS, Linux

**Application Structure**:
```
librecad/
├── src/
│   ├── actions/     # Drawing actions (line, circle, trim, etc.)
│   ├── cmd/         # Command line processor (AutoCAD-style)
│   ├── lib/         # Core geometry, math, DXF/DWG parsing
│   ├── main/        # Application entry, main window, MDI
│   └── plugins/     # Plugin system (C++ shared libraries)
├── plugins/         # Built-in plugins directory
└── desktop/         # Desktop integration files
```

**AutoCAD LT Compatibility** (Implemented):
An alias file (`landscape/autocad_aliases.txt`) maps 88 AutoCAD LT keyboard shortcuts to LibreCAD commands. Draw commands (L=Line, C=Circle, REC=Rectangle, PL=Polyline), modify commands (M=Move, CO=Copy, TR=Trim, O=Offset, MI=Mirror, RO=Rotate, SC=Scale), view commands (Z=Zoom, P=Pan), and utility commands (DI=Distance, AREA=Area, LA=Layer) all work as expected. A designer with AutoCAD LT muscle memory can sit down and start drafting immediately.

**Plugin Architecture** (5 landscape plugins registered):

| Plugin | Status | Description |
|--------|--------|-------------|
| AutoCAD Compatibility | Implemented | 88 command aliases matching AutoCAD LT 2014 |
| GIS Import | Planned | Import GeoTIFF, Shapefiles, KML/KMZ via GDAL |
| KIRI Scan Import | Planned | Import 3D scans from KIRI Engine, project to 2D |
| Plant Database | Planned | SQLite-backed searchable plant catalog with symbols |
| Irrigation Planning | Planned | Sprinkler/drip layout with coverage visualization |

All Netrun customizations reside in the `landscape/` directory, cleanly separated from upstream LibreCAD code to simplify ongoing upstream merges.

### Netrun CAD Web

**Status**: Implemented

Netrun CAD Web is a standalone single-page application built for touch-first design on iPad with Apple Pencil.

**Core Stack**:
- Framework: React 18 + TypeScript
- Canvas: HTML5 Canvas 2D API (chosen over SVG for performance with many strokes)
- Freehand Drawing: `perfect-freehand` 1.2 (Tldraw's pressure-sensitive stroke library)
- DXF Parsing: `dxf-parser` 1.1
- PDF Export: `jsPDF` 2.5
- GIS Data: `shapefile` 0.6
- Styling: Tailwind CSS 3.4
- Build: Vite 6
- Storage: localStorage (cloud save planned)

**Four Drawing Modes**:

1. **CAD Mode** — precise measurements with snap-to-grid, layers, lines, rectangles, circles, and dimensions. Keyboard and mouse optimized. Tools: select, line, rectangle, circle, dimension, move.

2. **Draw Mode** — Apple Pencil freehand sketching over CAD layers. Pressure-sensitive ink strokes via the `perfect-freehand` library. Brush types: pen, pencil, marker. Size, opacity, and color are adjustable per stroke.

3. **Color Mode** — watercolor and marker brushes for hand-coloring plans. Pressure controls opacity, producing natural wash effects. Brush types: watercolor, marker, fill. A landscape-specific color palette is built in.

4. **Text Mode** — fine-tip pen for architect-style handwritten lettering. Font size, family, color, and rotation are controllable per text element.

**Input Handling**:
The web app uses the PointerEvent API, which unifies mouse, touch, and Apple Pencil input into a single event model:
- `event.pressure` — Apple Pencil pressure (0.0 to 1.0), used for stroke width and opacity modulation
- `event.tiltX / event.tiltY` — pencil angle, available for future shading effects
- `getCoalescedEvents()` — high-frequency point sampling for smooth, artifact-free strokes
- `touch-action: none` CSS prevents browser gestures from interfering with drawing

**Data Model**:
The drawing engine supports seven element types: `CADLine`, `CADRectangle`, `CADCircle`, `CADDimension`, `FreehandStroke`, `TextElement`, and `PlantPlacement`. All elements are assigned to layers and carry full style metadata (stroke color, width, fill, opacity, brush type).

Nine default layers are preconfigured for landscape plan conventions:

| Layer | Purpose | Default Color |
|-------|---------|---------------|
| Scan | Imported 3D scan data | Orange |
| GIS | Basemap and property boundaries | Cyan |
| Site | Property lines, existing features | Gray |
| Hardscape | Paths, patios, walls, structures | Brown |
| Planting | Plant placements and symbols | Green |
| Irrigation | Sprinkler/drip layouts | Blue |
| Drawing | Freehand pencil sketches | Dark gray |
| Color | Watercolor/marker washes | Green |
| Text | Labels and annotations | Black |

**GIS Basemap** (Implemented):
A satellite basemap panel provides address geocoding (via Nominatim), tile rendering from Esri or OpenStreetMap, zoom and opacity controls, scale calibration, and a lock toggle to prevent accidental basemap movement while drawing.

**GIS Import** (Implemented):
GeoJSON and KML file import converts vector property boundaries, parcels, and site features into CAD elements on the GIS layer.

**3D Scan Import** (Implemented):
OBJ and PLY files exported from KIRI Engine are imported and processed through a scan pipeline that:
- Projects 3D vertices to 2D plan view (X/Z plane, dropping the Y/up axis)
- Converts meters to feet (KIRI exports in meters)
- Generates output in three modes: point cloud visualization, convex hull boundary detection, and elevation contour lines at configurable intervals
- All processing runs in a Web Worker to avoid blocking the UI thread

**DXF Import** (Implemented):
DXF files are parsed via the `dxf-parser` library and converted to native CAD elements, enabling import of existing drawings from AutoCAD, LibreCAD, or other CAD tools.

**DXF Export** (Implemented):
The current drawing can be exported as DXF for round-trip compatibility with desktop CAD applications.

**PDF Export** (Implemented):
Scaled PDF output supports standard landscape plan scales (1/4"=1', 1/8"=1', 1/16"=1', 1"=10') and page sizes (ARCH D, ARCH E, Letter). The renderer produces high-resolution raster output via jsPDF.

### Shared Resources

Both desktop and web products share foundational data assets:

- **Plant Database** — 59 species for USDA Zone 9b with botanical names, WUCOLS water use ratings, sun exposure, mature dimensions, native status, drought/deer/fire resistance (CSV for desktop, JSON for web)
- **DXF Symbol Library** — 45 plan-view symbols (5 imported from open-source sources, 40 programmatically generated)
- **Layer Conventions** — standardized layer names, colors, and ordering for landscape plan drawings
- **AutoCAD Command Aliases** — 88 keyboard shortcuts for CAD workflow consistency

---

## 4. The Touch-First Design Workflow

Allie Garza is a landscape designer based in Ojai, California. She has designed residential outdoor spaces for over a decade, working with California native plants, Mediterranean species, and the particular constraints of Southern California — drought, fire risk, deer, and extreme summer heat. Her workflow, like most landscape designers, has always included a manual drawing step. Netrun CAD Web was designed to eliminate it.

### The Old Workflow

1. **Site visit**: Walk the property, take measurements, note existing trees and features
2. **CAD drafting** (AutoCAD LT, desktop): Draw the base plan — property boundary, structures, hardscape, existing trees
3. **Print**: Send the CAD drawing to a large-format printer (24x36 minimum)
4. **Hand draw**: Using colored pencils and markers on the printed plan, draw planting symbols, annotate species, add color washes for material indication
5. **Scan**: Photograph or flatbed-scan the hand-drawn plan back into digital format
6. **Deliver**: Email the scanned PDF to the client

This workflow produces beautiful plans — hand-drawn planting has an organic quality that CAD cannot replicate. But it is slow, wasteful, and fragile. Every revision requires reprinting, redrawing, and rescanning. The artistic layer exists only on paper.

### The Netrun CAD Workflow

1. **Site visit**: Walk the property with iPad. Optionally scan features with KIRI Engine
2. **Import** (Netrun CAD Web): Load satellite basemap by entering the property address. Import KIRI scan as site survey. Import GeoJSON property boundary
3. **CAD draft** (Mode 1): Draw hardscape layout — paths, patios, walls, structures — using line, rectangle, and circle tools with snap-to-grid. Add dimensions
4. **Sketch planting** (Mode 2): Switch to Draw mode. Using Apple Pencil, sketch planting symbols directly on the Planting layer. The pen responds to pressure — light strokes for groundcover, heavy strokes for tree canopies. No printing required
5. **Color** (Mode 3): Switch to Color mode. Apply watercolor washes — terracotta for DG paths, sage green for native plantings, blue for water features. Pressure controls opacity for natural layering effects
6. **Label** (Mode 4): Switch to Text mode. Add plant labels, notes, dimensions in architect-style handwriting
7. **Export**: Generate a scaled PDF (1/4"=1', ARCH D) or DXF file. Send directly to the client from iPad

The entire process stays digital. Every stroke is editable. Revisions do not require reprinting. The artistic hand-drawn quality is preserved through pressure-sensitive freehand drawing — but the drawing lives in a layered, exportable, version-controlled digital file.

---

## 5. Environmental Intelligence

### Landscape Element Database

The landscape element database (`landscape_elements_complete.csv`) catalogs 84 elements across 9 categories, representing the complete vocabulary of a Southern California residential landscape plan:

| Category | Count | Examples |
|----------|-------|---------|
| Hardscape (surfaces + structures + edges) | 23 | Decomposed granite, flagstone, permeable pavers, retaining walls, pergolas, fire pits, steel edging |
| Shrubs (native) | 10 | Ceanothus, Manzanita, White Sage, Black Sage, Lemonade Berry, Coffeeberry, Cleveland Sage |
| Trees (native) | 10 | Coast Live Oak, Valley Oak, California Sycamore, Toyon, Desert Willow, Western Redbud, California Fan Palm |
| Irrigation | 9 | Drip emitters, spray heads, rotor heads, bubblers, valve boxes, controllers, rain sensors |
| Existing site features | 9 | Existing oaks, sycamores, boulders, rock outcrops, retaining walls, fences, utility boxes, drainage, slopes |
| Groundcovers | 8 | Creeping Sage, Dymondia, Dwarf Coyote Brush, Blue Fescue, Deer Grass, Red Fescue, Yarrow, Sedge |
| Shrubs (adapted) | 6 | Lavender, Rosemary, Agave, Aloe, Rockrose, Pride of Madeira |
| Trees (adapted) | 5 | Olive, Italian Cypress, Jacaranda, Brisbane Box, Crape Myrtle |
| Lighting | 4 | Path lights, spot/uplights, wall sconces, string lights |

Every element includes metadata: symbol type, symbol style, movability (existing features cannot be moved), typical size, material, drought score (0-10), maintenance level, fire resistance, and ADA accessibility.

### Plant Database

The plant database (`plant_database_ojai_zone9b_v1.0.csv`) contains 59 species specifically curated for the Ojai Valley and Ventura County (USDA Zone 9b):

| Category | Count | Example Species |
|----------|-------|-----------------|
| Native California trees | 10 | Coast Live Oak, Valley Oak, California Sycamore, Toyon, Desert Willow, California Buckeye, Blue Oak |
| Mediterranean/adapted trees | 11 | Olive, Italian Cypress, Jacaranda, Palo Verde, Canary Island Date Palm, Ginkgo |
| Native California shrubs | 11 | Ceanothus, Manzanita, California Sagebrush, White Sage, Black Sage, Coffeeberry, Buckwheat |
| Mediterranean/adapted shrubs | 13 | Lavender, Rosemary, Agave, Aloe, Bougainvillea, Rockrose, Texas Sage, Prickly Pear |
| Groundcovers and grasses | 10 | Deer Grass, Blue Fescue, Dymondia, Dwarf Coyote Brush, Yarrow, Red Fescue |
| Perennials and accents | 4 | Hummingbird Sage, California Poppy, Red Hot Poker, Toyon (groundcover cultivar) |

**California native representation**: 30 of 59 species (51%) are native to California. The remaining 29 are drought-adapted Mediterranean, South African, or Australian species proven in Southern California landscapes.

**WUCOLS Water Use Integration**:
Every plant carries a WUCOLS water use classification — the standard used by California water agencies for landscape water budgets:
- **VL (Very Low)**: 36 species — survive on rainfall alone once established
- **L (Low)**: 20 species — minimal supplemental irrigation
- **M (Moderate)**: 3 species — regular irrigation required

This distribution reflects intentional curation for drought-tolerant design. A designer placing plants from this database will produce inherently water-efficient landscapes.

**Resistance Ratings**:
Each species is classified for drought tolerance, deer resistance, and fire resistance — the three primary threats to Ojai Valley landscapes. A designer can filter by these attributes when selecting species for specific site conditions (wildland-urban interface fire zones, properties with deer pressure, unirrigated slopes).

**Data Sources** (verified): WUCOLS V (UC Davis), Las Pilitas Nursery, Theodore Payne Foundation, Calscape (California Native Plant Society), USDA PLANTS Database, UC Davis Arboretum All-Stars.

The web application includes a separate curated database of 24 Southern California plants with canopy color metadata for plan-view rendering, enabling color-accurate plant placement on digital drawings.

---

## 6. GIS and 3D Scan Integration

### Satellite Basemap (Implemented — Web)

The web application includes a satellite basemap panel that provides:

- **Address geocoding**: Enter a street address to center the map on a property (via Nominatim/OpenStreetMap geocoding API)
- **Tile providers**: Esri World Imagery (satellite) and OpenStreetMap (street map) tile sources
- **Zoom control**: Adjustable tile zoom level for appropriate detail
- **Opacity slider**: Fade the basemap behind CAD layers for tracing
- **Scale calibration**: Displays feet-per-pixel at the current zoom level
- **Lock toggle**: Prevent accidental basemap pan while drawing

This replaces the need for a separate GIS tool or Google Earth session to establish site context. A designer can enter a property address, see the satellite view, and begin tracing property features directly.

### GIS Vector Import (Implemented — Web)

GeoJSON and KML files can be imported to place property boundaries, parcels, easements, and other vector features on the GIS layer. This supports:

- County assessor parcel exports (typically GeoJSON)
- Google Earth KML exports (property outlines, site markers)
- Surveyor data in standard GIS formats

Imported features are converted to native CAD elements (lines, polylines) and placed on the GIS layer for reference.

### KIRI Engine 3D Scan Import (Implemented — Web; Planned — Desktop)

KIRI Engine is an iOS app that produces photogrammetric 3D scans from iPhone or iPad camera footage. Landscape designers use it to capture existing site conditions — mature trees, boulder formations, retaining walls, grade changes — that are difficult to measure manually.

Netrun CAD Web imports OBJ and PLY files from KIRI Engine and processes them through a scan pipeline:

1. **3D to 2D Projection**: Vertices are projected to plan view by dropping the Y axis (up) and mapping X/Z to the 2D drawing plane
2. **Unit Conversion**: KIRI exports in meters; the processor converts to feet (scale factor 3.28084, configurable)
3. **Three Output Modes**:
   - **Point Cloud**: Raw vertex positions rendered as dots on the Scan layer, showing the full scan footprint
   - **Boundary Detection**: Convex hull algorithm generates a site boundary polyline from the scan extent
   - **Elevation Contours**: Contour lines generated at configurable elevation intervals (default 1 foot), showing grade changes across the site
4. **Web Worker Processing**: All computation runs in a Web Worker thread to avoid blocking the drawing UI during large scan imports

The desktop plugin (`kiri_import`) will provide the same functionality within the LibreCAD environment, with the addition of GDAL-powered coordinate system transformations.

### Planned GIS Enhancements (Desktop)

The GIS Import plugin for the desktop application will support:
- GeoTIFF raster import (aerial photography, topographic maps)
- Shapefile (.shp) import via GDAL/OGR
- KML/KMZ import
- Coordinate system projection and transformation

---

## 7. Symbol Library

### Current State

The symbol library contains **45 DXF plan-view symbols** ready for use in landscape drawings:

- **5 imported symbols**: From the open-source `growdigital/blocks-forestgarden` repository (DXF R2013 format, LibreCAD-compatible). These cover basic canopy tree and shrub forms for forest garden design.
- **40 programmatically generated symbols**: Created via Python scripts using the `ezdxf` library. These cover geometric elements — hardscape surfaces (DG stipple, flagstone joints, gravel patterns), hardscape structures (retaining walls, fire pits, pergolas), irrigation components (spray heads, drip emitters, valve boxes), lighting (path lights, uplights, sconces), and site features (fences, utility boxes, drainage arrows).

### Generation Methods

Three methods are used to create symbols, each suited to different element types:

1. **Artist-Drawn** (Priority 1 — 15 species): Allie draws plan-view canopy shapes directly in LibreCAD for the most-used species. Hand-drawn symbols have the organic quality that landscape plans require — no two trees look the same. Priority species include Coast Live Oak, Valley Oak, California Sycamore, Olive, Toyon, Ceanothus, Manzanita, Agave, and Deer Grass.

2. **Programmatic Generation** (Priority 2 — 40 symbols, complete): Geometric elements are generated as DXF files via Python/ezdxf scripts. Hardscape fill patterns, irrigation symbols, lighting symbols, and site features are geometric by nature and produce consistent, standards-compliant output.

3. **AI-Assisted** (Priority 3 — complex patterns): Fill patterns requiring natural randomness (decomposed granite stipple, flagstone joint patterns, gravel textures) can be generated as SVG reference patterns and traced or converted to DXF.

### Gap Analysis

No open-source DXF symbol library exists specifically for California native plants. Generic tree symbols (circular canopy outlines) exist in abundance, but species-specific representations — the distinctive radial fronds of California Fan Palm, the columnar dot of Italian Cypress, the irregular evergreen mass of Coast Live Oak — do not exist as freely available CAD blocks.

Netrun CAD is building the first open-source California native plant symbol library. The 84 elements in the landscape database are mapped for future symbol generation, with symbol standards defined:

- **Scale**: 1:1 (1 drawing unit = 1 foot)
- **Layer assignment**: `TREE-NATIVE`, `TREE-ADAPTED`, `SHRUB-NATIVE`, `SHRUB-ADAPTED`, `GROUNDCOVER`, `HARDSCAPE`, `IRRIGATION`, `LIGHTING`, `EXISTING`
- **File naming**: `tree_coast_live_oak_30ft.dxf`, `shrub_ceanothus_6ft.dxf`, `irrigation_spray_quarter.dxf`
- **Block naming**: Matches the `symbol_file` column in both database CSV files for programmatic insertion

---

## 8. Open Source Strategy

### License

Netrun CAD Desktop inherits the GPLv2 license from LibreCAD. All modifications, plugins, and landscape extensions are released under the same license. The web application follows the same open-source commitment.

### Upstream Separation

All Netrun customizations reside in the `landscape/` directory and `plugins/` directory, clearly separated from upstream LibreCAD source code. This design decision enables:

- **Clean upstream merges**: `git fetch upstream && git merge upstream/master` incorporates LibreCAD improvements without conflicts in Netrun-specific code
- **Two-branch strategy**: `master` branch tracks upstream LibreCAD; `landscape-design` branch contains all Netrun additions
- **Plugin isolation**: Landscape features are implemented as C++ plugins loaded at runtime, not modifications to core LibreCAD code

### Community Contribution Model

The plant database, symbol library, and landscape element catalog are designed as community-extensible resources:

- Plant database CSV files can be forked and adapted for any USDA zone or climate region
- DXF symbol files follow documented naming and scale standards for consistent contribution
- The plugin registry (`landscape/plugins/registry.json`) defines a schema for third-party landscape extensions

### What We Contribute Back

The Netrun CAD project contributes to the open-source ecosystem:

- The first open-source California native plant symbol library for CAD
- A curated Zone 9b plant database with WUCOLS water use integration
- An 84-element landscape vocabulary with metadata (drought scores, fire resistance, ADA compliance)
- Documentation of the AutoCAD LT to LibreCAD migration path for landscape professionals

---

## 9. Technical Specifications

### Desktop Application

| Component | Specification |
|-----------|--------------|
| Language | C++17 |
| UI Framework | Qt6 |
| Build System | CMake |
| License | GPLv2 |
| Platforms | Windows, macOS, Linux |
| File Formats (Read) | DXF R2013, DWG (via ODA converter) |
| File Formats (Write) | DXF R2013 |
| Dependencies | CMake, Qt6, Boost, FreeType, muparser |
| Plugin System | C++ shared libraries (.so/.dll/.dylib) |
| Database | SQLite (plant database plugin) |
| Build Pipeline | Azure DevOps (Windows), GitHub Actions (macOS/Linux) |

### Web Application

| Component | Specification |
|-----------|--------------|
| Framework | React 18.3 + TypeScript 5.7 |
| Build Tool | Vite 6.0 |
| Canvas | HTML5 Canvas 2D API |
| Freehand Library | perfect-freehand 1.2 |
| DXF Parser | dxf-parser 1.1 |
| PDF Generator | jsPDF 2.5 |
| GIS Data | shapefile 0.6 |
| Styling | Tailwind CSS 3.4 |
| Input | PointerEvent API (mouse, touch, Apple Pencil) |
| Storage | localStorage (cloud save planned) |
| Deployment | Cloud Run (planned) |

### File Format Support

| Format | Read | Write | Notes |
|--------|------|-------|-------|
| DXF R2013 | Desktop + Web | Desktop + Web | Native format |
| DWG | Desktop (via ODA) | No | AutoCAD compatibility |
| PDF | No | Web | Scaled output (1/4"=1', 1/8"=1', 1/16"=1', 1"=10') |
| OBJ | Web | No | KIRI Engine 3D scan import |
| PLY | Web | No | KIRI Engine 3D scan import |
| GeoJSON | Web | No | Property boundary import |
| KML | Web | No | Google Earth import |
| Shapefile | Web | No | County assessor data |

### Page Sizes (PDF Export)

Standard landscape plan output sizes: ARCH D (24x36"), ARCH E (36x48"), Letter (8.5x11"). Landscape orientation. Scale options: 1/4"=1' (1:48) for residential detail, 1/8"=1' (1:96) for residential overview, 1/16"=1' (1:192) for large sites, 1"=10' (1:120) for site plans.

---

## 10. Roadmap

### Phase 1: Core Platform (Complete)

- LibreCAD fork with landscape-design branch
- 88 AutoCAD LT command aliases (implemented)
- Web application with 4 drawing modes (CAD, Draw, Color, Text)
- Apple Pencil pressure sensitivity via PointerEvent API
- perfect-freehand integration for natural ink strokes
- 59-species Zone 9b plant database (CSV + JSON)
- 84-element landscape element database
- 45 DXF plan-view symbols (5 imported, 40 generated)
- 9 preconfigured landscape plan layers
- Undo/redo history
- Plant browser with search and filtering
- Keyboard shortcuts matching AutoCAD conventions

### Phase 2: Import/Export and Site Data (Implemented — Web)

- DXF import and export
- Scaled PDF export (ARCH D/E, multiple scales)
- GIS satellite basemap with address geocoding
- GeoJSON and KML import for property boundaries
- KIRI Engine OBJ/PLY 3D scan import
- Scan-to-2D projection (plan view, boundary detection, contour generation)
- Shapefile import

### Phase 3: Desktop Plugins and Cloud (Planned)

- Desktop GIS Import plugin (GeoTIFF, Shapefile, KML via GDAL)
- Desktop KIRI Scan Import plugin (OBJ/PLY to 2D)
- Desktop Plant Database plugin (SQLite-backed, searchable catalog)
- Desktop Irrigation Planning plugin (coverage visualization, GPM calculations)
- Cloud save via Express backend + PostgreSQL (web)
- User authentication (web)

### Phase 4: Intelligence and Automation (Future)

- AI-assisted planting suggestions based on site conditions (sun, water, soil)
- Irrigation zone auto-design from plant water use data
- Material quantity takeoffs and cost estimation
- Water budget calculator for MWELO compliance
- WUCOLS V direct database integration

### Phase 5: Collaboration and Delivery (Vision)

- Multi-user project collaboration
- Client review portal with annotation
- AR site visualization (view proposed design overlaid on real site via iPad camera)
- Contractor bid integration (material lists, labor estimates)
- GDAL-powered coordinate system integration for professional surveyor data

---

## 11. About Netrun Systems

**Netrun Systems** is a California C Corporation, incorporated May 2025. The company builds cloud infrastructure, AI platforms, and design tools under an open-source-first philosophy.

**Daniel Garza**, Founder and CEO, brings 25 years of professional experience in cloud infrastructure, DevSecOps, and multi-tenant management platforms. He has consulted through www.netrun.net since 2001, building enterprise systems for organizations across financial services, transportation, and technology sectors. Netrun CAD applies that infrastructure expertise — build systems, CI/CD pipelines, plugin architectures, data modeling — to a design tool that solves a real problem for a real user.

**Allie Garza**, Landscape Designer and Product Visionary, is the reason Netrun CAD exists. Her return to landscape design practice after years away from AutoCAD LT — and her frustration with the cost, workflow limitations, and lack of plant intelligence in existing tools — defined every product decision. She is a professional artist whose hand-drawn planting plans are the aesthetic standard the digital tools must match. The plant database reflects her personal plant palette, refined over years of designing for the Ojai Valley climate. The Apple Pencil integration exists because she draws every day.

**Open Source Commitment**: Netrun CAD is released under GPLv2. The plant database, symbol library, and landscape element catalog are freely available for any designer, firm, or educational institution to use, modify, and extend. The project's goal is not to lock designers into a proprietary platform but to give them professional-grade tools they can own.

---

*Document Version: 1.0*
*Date: March 22, 2026*
*Repository: [Netrun-Systems/netrun-cad](https://github.com/Netrun-Systems/netrun-cad)*
*Web Application: [Netrun-Systems/netrun-cad-web](https://github.com/Netrun-Systems/netrun-cad-web)*
*License: GPLv2*
*Contact: Daniel Garza, daniel@netrunsystems.com*
