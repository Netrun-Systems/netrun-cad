# Netrun CAD — Landscape Plugin Architecture

Landscape-specific plugins for Allie Garza's landscape design practice, built on top of LibreCAD's C++ plugin system.

## Overview

LibreCAD loads plugins at startup from the `plugins/` directory next to the executable. Each plugin is a C++ shared library (`.dll` on Windows, `.so` on Linux, `.dylib` on macOS) that implements `QC_PluginInterface` and is discovered via Qt's plugin system (`Q_PLUGIN_METADATA`).

All Netrun landscape plugins live in `landscape/plugins/` and are compiled into the same output directory as the upstream LibreCAD plugins. No core LibreCAD files are modified.

---

## Plugin Interface

Every plugin inherits from `QC_PluginInterface` (defined in `librecad/src/plugins/qc_plugininterface.h`):

```cpp
class QC_PluginInterface {
public:
    virtual ~QC_PluginInterface() {}
    virtual QString name() const = 0;
    virtual PluginCapabilities getCapabilities() const = 0;
    virtual void execComm(Document_Interface *doc, QWidget *parent, QString cmd) = 0;
};
```

`getCapabilities()` returns menu entry points (which Plugins menu item triggers the plugin).
`execComm()` is called when the user activates the plugin — show a dialog, run a command, etc.
`Document_Interface` provides access to the active drawing (add lines, arcs, blocks, layers, etc.).

---

## Plugin Directory Structure

Each plugin follows this layout:

```
landscape/plugins/plugin_name/
├── CMakeLists.txt          # qt_add_plugin() target; links Qt6::Core + Qt6::Widgets
├── plugin_name.h           # Class declaration (inherits QC_PluginInterface)
├── plugin_name.cpp         # Implementation
├── plugin_name.json        # Qt plugin metadata (IID, Name, Version, Keys)
├── plugin_name.rc          # Windows version resource (VERSIONINFO)
└── resources/              # Icons, SQLite DB seeds, data files (future)
```

---

## Plugin Registry

`registry.json` in this directory is the authoritative list of Netrun landscape plugins.

| Plugin | Display Name | Status | Key Commands |
|--------|-------------|--------|--------------|
| `gis_import` | GIS Import | planned | gisimport, importshp, importkml |
| `kiri_import` | KIRI Scan Import | planned | kiriimport, scanview |
| `plant_database` | Plant Database | planned | plantdb, insertplant, plantschedule |
| `irrigation` | Irrigation Planning | planned | irrigation, sprinkler, dripcircle, coverage |
| `autocad_compat` | AutoCAD Compatibility | ready | (keybinding layer, no commands) |

---

## Adding a New Plugin

1. Create `landscape/plugins/my_plugin/` with the four files above.
2. Add `add_subdirectory(landscape/plugins/my_plugin)` to the main `CMakeLists.txt` inside the `BUILD_LANDSCAPE_PLUGINS` block.
3. Add an entry to `registry.json`.
4. Name the IID `"org.netrun.netrun-cad.my_plugin"` in the JSON metadata.
5. Use `qt_add_plugin(my_plugin SHARED ...)` — not `add_library()` — so Qt's plugin loader can find it.

---

## Build (Windows / MSVC)

```bat
cmake -S . -B build ^
  -G "Visual Studio 17 2022" ^
  -DCMAKE_PREFIX_PATH="C:\Qt\6.9\msvc2022_64" ^
  -DBUILD_LANDSCAPE_PLUGINS=ON
cmake --build build --config Release
```

Plugin DLLs land in `build\Release\plugins\`. The Azure DevOps pipeline (`azure-pipelines.yml`) handles this automatically.

---

## Build (macOS)

```bash
cmake -S . -B build \
  -DCMAKE_PREFIX_PATH="$(brew --prefix qt@6)" \
  -DBUILD_LANDSCAPE_PLUGINS=ON
cmake --build build -j$(nproc)
```
