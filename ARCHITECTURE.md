# Netrun CAD — Architecture

**Repository**: `netrun-cad` (Netrun Systems)
**Upstream**: [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD) (GPLv2)
**Branch convention**: `landscape-design` (Netrun customizations), `master` (upstream sync)
**Target user**: Allie Garza — landscape designer returning to practice after AutoCAD LT 2014; works on macOS

**Role**: SECONDARY. The primary tool is `netrun-cad-web` (web-based CAD, separate repo). This desktop fork exists for offline / advanced 2D drafting workflows that the web app doesn't cover. The desktop build is currently broken on Windows (known gap per `CURRENT_STATE.md` — pipeline file present, build failing).

---

## 1. Repository structure

```mermaid
flowchart TB
    subgraph Upstream["LibreCAD upstream (master branch)"]
        UCMAKE[CMakeLists.txt]
        ULIBR[librecad/<br/>core LibreCAD]
    end

    subgraph LibreCAD_Core["librecad/src/ (upstream)"]
        ACTIONS[actions/<br/>line, circle, trim, etc.]
        CMD[cmd/<br/>command line processor<br/>AutoCAD-like CLI]
        LIB[lib/<br/>core geometry + DXF/DWG]
        MAIN[main/<br/>app entry + MDI window]
        UPLUGINS[plugins/<br/>plugin SDK]
        UTEST[test/<br/>unit tests]
    end

    subgraph Netrun["Netrun additions (landscape-design branch)"]
        AUTOCAD[plugins/autocad_compat/<br/>AutoCAD LT keybindings<br/>L/C/M/TR/O aliases]
        GIS[plugins/gis_import/<br/>GeoTIFF + Shapefile + KML/KMZ<br/>via GDAL/OGR]
        KIRI[plugins/kiri_import/<br/>OBJ/PLY scan import<br/>+ 2D plan projection]
        PLANT[plugins/plant_database/<br/>SQLite plant catalog<br/>zones, water, spacing]
        IRRIG[plugins/irrigation/<br/>sprinkler placement<br/>GPM calc, zones]
        LANDSCAPE[landscape/<br/>40 DXF symbols<br/>SYMBOL_GENERATION_PLAN.md]
    end

    subgraph Build["Build + CI"]
        CMAKE_USER[CMakePresets.json]
        AZP[azure-pipelines.yml]
        WINBUILD[Windows build<br/>currently failing]
    end

    subgraph Docs["User-facing docs"]
        ALLIE[ALLIE_GETTING_STARTED<br/>.md + .docx]
        WHITE[NETRUN_CAD_WHITEPAPER.md<br/>investor/partner overview]
        CHANGE[CHANGELOG.md + ChangeLogs/]
    end

    Upstream --> LibreCAD_Core
    LibreCAD_Core --> Netrun
    Netrun --> Build
    Build -.failing.-> WINBUILD

    classDef broken fill:#fdd,stroke:#c33,color:#900,stroke-dasharray:4 2;
    classDef secondary fill:#eef,stroke:#88a,color:#446;
    class WINBUILD broken;
    class Netrun secondary;
```

---

## 2. Plugin design principle

**All Netrun additions are isolated in `plugins/`** so upstream sync from LibreCAD remains low-friction. Per CLAUDE.md: "Keep all Netrun customizations in plugins/ or clearly marked sections to simplify upstream merging."

The 5 Netrun plugins are independent shared libraries loaded by LibreCAD's plugin system.

```mermaid
flowchart LR
    A[autocad_compat] -- L/C/M/TR/O --> CMD[src/cmd/rs_commands.cpp]
    G[gis_import] -- via GDAL/OGR --> LIB[lib/fileio]
    K[kiri_import] -- OBJ/PLY parser --> LIB
    P[plant_database] -- SQLite + symbols --> BLOCKS[LibreCAD blocks]
    I[irrigation] -- coverage circles + GPM --> ACTIONS_DIR[actions/]
```

---

## 3. Build commands

```bash
# macOS (Allie's platform — works)
brew install cmake qt@6 boost freetype
mkdir build && cd build
cmake .. -DCMAKE_PREFIX_PATH=$(brew --prefix qt@6)
make -j$(nproc)
./desktop/LibreCAD

# Ubuntu/Debian
sudo apt install cmake qt6-base-dev libboost-all-dev libfreetype-dev
mkdir build && cd build && cmake .. && make -j$(nproc)
```

The Windows build (`azure-pipelines.yml`) is currently failing — known gap. macOS and Linux builds are functional.

---

## 4. Role vs netrun-cad-web

```mermaid
flowchart TB
    USER[Allie Garza<br/>landscape designer]
    USER -->|primary, daily work| WEB[netrun-cad-web<br/>web app]
    USER -.->|advanced drafting, offline,<br/>DWG/DXF interop| DESKTOP[netrun-cad<br/>this repo]
    WEB -.shared catalog.-> DESKTOP

    classDef secondary fill:#eef,stroke:#88a,color:#446,stroke-dasharray:4 2;
    class DESKTOP secondary;
```

Per the `project_netrun_cad_allie.md` memory: netrun-cad / netrun-cad-web is an internal revenue SKU; Allie is Daniel's spouse + business partner, not a reference user; cad-web is the priority that needs to ship for paid landscape work. This desktop fork is the secondary path.

---

## 5. Key files

- `CMakeLists.txt` + `CMakePresets.json` — build configuration
- `librecad/src/cmd/rs_commands.cpp` — command aliases (AutoCAD mapping landing zone)
- `librecad/src/main/qc_applicationwindow.cpp` — main window + toolbars
- `librecad/src/lib/fileio/` — DXF/DWG I/O
- `plugins/{autocad_compat,gis_import,kiri_import,plant_database,irrigation}/` — Netrun plugins
- `landscape/` — DXF symbol library + generation plan
- `azure-pipelines.yml` — Windows CI (currently failing)
- `NETRUN_CAD_WHITEPAPER.md` — platform overview for investors / partners
- `ALLIE_GETTING_STARTED.md` — user onboarding

See `CLAUDE.md` for upstream sync guidance and full plugin descriptions.
