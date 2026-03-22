# RESEARCH_PLANT_SYMBOLS_REPORT_v1.0

**Research Domain**: Landscape Architecture CAD Resources
**Scope**: Plant symbol libraries, plant databases, California-specific resources
**Target Use**: Netrun CAD (LibreCAD fork) — Allie Garza Landscape Architecture, Ojai CA (Zone 9b)
**Date**: 2026-03-22
**Correlation ID**: research_20260322_plant-symbols_LA001

---

## 1. Context Validation

- [x] Research scope: CAD plant symbols + plant databases for Zone 9b Mediterranean landscape
- [x] Source credibility: Official government databases, established CAD repositories, university sources
- [x] Recency: WUCOLS V is current (live as of March 25, 2025); CAD block sources verified active
- [x] Decision context: Populate Netrun CAD with landscape design assets for professional practice

---

## 2. Summary of Findings

Three categories of resources were identified and evaluated:

1. **CAD Symbol Libraries** — Free DWG/DXF block collections for import into LibreCAD
2. **Plant Databases** — Structured botanical data (names, zones, water use, size)
3. **California-Specific Resources** — WUCOLS, Calscape, native plant databases

---

## 3. CAD Plant Symbol Libraries

### 3A. GitHub / Open Source

---

#### growdigital/blocks-forestgarden
- **URL**: https://github.com/growdigital/blocks-forestgarden
- **Format**: DXF R27 (2013) — fully LibreCAD compatible
- **License**: Check repo LICENSE file (public GitHub, no commercial restriction noted)
- **Contents**: 5 categories of forest garden plant blocks:
  - Canopy trees
  - Shrubs
  - Perennials
  - Annuals
  - Climbers
- **Features**: Blocks include labels with plant diameter, abbreviation, and type. Labels are on a separate layer (can be hidden in presentation drawings). Based on Martin Crawford's *Creating a Forest Garden*.
- **Relevance**: Moderate — temperate forest garden focus, not Southern California specific. Canopy and shrub symbols are reusable for any plan-view landscape drawing.
- **How to access**: `git clone https://github.com/growdigital/blocks-forestgarden` — DXF files import directly into LibreCAD via File > Import.

---

#### GSStnb/dxfBlocks
- **URL**: https://github.com/GSStnb/dxfBlocks
- **Format**: DXF — designed specifically for LibreCAD
- **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
  - Free for personal/non-commercial use
  - **Commercial use restricted** — landscape firm billable work may require separate arrangement
- **Contents**: Architecture category includes a "Landscaping" sub-collection. Full list requires browsing the repo.
- **Features**: All geometry on layer '0', drawn full-scale in inches, ready for LibreCAD block insertion
- **Relevance**: Low-to-moderate for plant symbols specifically; better for hardscape elements
- **How to access**: `git clone https://github.com/GSStnb/dxfBlocks` — browse `Architecture/Landscaping/`

---

### 3B. Free CAD Block Websites

---

#### dwgshare.com — Tree and Plant Plan View Collection
- **URL**: https://dwgshare.com/47-free-cad-blocks-tree-plant-symbols-for-plan-view/
- **Format**: DWG (AutoCAD 2018+) — import into LibreCAD via File > Import
- **License**: No registration required; specific commercial terms not stated — verify before client deliverables
- **Contents**: Hundreds of tree and shrub symbols in plan view (top-down), including:
  - Shade trees (simple geometric to complex organic linework)
  - Ornamental trees
  - Shrubs
- **File size**: ~978 KB single DWG file
- **Download**: Direct download via Google Drive link on page
- **Relevance**: High — plan-view focus matches landscape architecture use case

---

#### cad-blocks.net — Vegetation Collection
- **URL**: https://cad-blocks.net/vegetation-cad-blocks.html
- **Format**: DWG (individual blocks)
- **License**: Not explicitly stated per block category; site provides free downloads
- **Contents**: 1,168 total vegetation CAD blocks including:
  - 437 trees in plan view
  - 64 color trees in plan view
  - Trees in elevation
  - Potted plants, bushes, palms
  - Simple trees, conifers
- **Relevance**: High — large collection, plan-view trees directly usable. No specific California/succulent category noted but general palm and shrub symbols present.
- **How to access**: Browse by category on site; individual block downloads

---

#### cadblocksdwg.com — Landscape Collection
- **URL**: https://www.cadblocksdwg.com/landscape.html
- **Format**: DWG
- **License**: Free download; no explicit commercial restriction stated
- **Contents**:
  - Cypress trees (7 blocks)
  - Palms
  - Conifer/pine/fir trees
  - Shrubs and bushes
  - Cactus blocks
  - Trees in plan view
  - Pots and planters
- **Relevance**: High — includes cacti and palms, directly relevant to Ojai/Southern California landscapes

---

#### freecads.com — Landscape Collection
- **URL**: https://www.freecads.com/cad-category/landscape/
- **Format**: DWG, DXF, PDF (multiple format options per file)
- **License**: Free with optional premium membership (EUR 2.90/month). Free tier allows unlimited downloads. Creative-commons-style attribution may apply per upload.
- **Contents**:
  - Tree plan views ("Tree with Low Level of Detail – Plan View", "Tree Top Plan View")
  - Planting edging
  - Rocks and boulders
  - Site elements
- **Relevance**: Moderate — good general collection; plan-view trees available

---

#### firstinarchitecture.co.uk — Plants and Shrubs
- **URL**: https://www.firstinarchitecture.co.uk/free-cad-blocks-plants-and-shrubs/
- **Format**: DWG (metric and imperial versions)
- **License**: Free for use by anyone. **Do not redistribute or resell.** Provided "as seen."
- **Contents**: Shrubs, groundcover, ferns, ornamental grasses, small shrubbery — plan view for site plans and presentation drawings
- **Relevance**: High for groundcover and shrub symbols specifically

---

#### pincad.com — Succulents DWG
- **URL**: https://pincad.com/succulents-dwg/
- **Format**: DWG
- **License**: Advertised as free; specific terms not fully visible
- **Contents**: Succulent plant symbols in top and elevation views — suitable for patio plans and commercial landscaping
- **Relevance**: High — succulents are essential for Ojai/Zone 9b designs

---

#### cadblocksforfree.com — Cactus and Desert Plants
- **URL**: https://www.cadblocksforfree.com/landscaping-and-garden/CADBLOCKSFORFREE0000468/
- **Format**: DWG (AutoCAD 2000 format — broadest compatibility including LibreCAD)
- **License**: Free; check individual block terms
- **Contents**: Cacti and desert plant blocks in elevation view
- **Relevance**: High — desert/arid plant symbols directly applicable to Southern California

---

#### linecad.com — Trees and Plant CAD Blocks
- **URL**: https://linecad.com/trees-and-plant-cad-blocks-free-dwg-download-for-autocad/
- **Format**: DWG
- **License**: Not explicitly stated
- **Contents**:
  - Deciduous trees (plan + elevation)
  - Palm trees (plan + elevation)
  - Coniferous trees
  - Shrubs, bushes
  - Flowering plants
  - Groundcover
- **Relevance**: High — comprehensive multi-type collection including palms

---

#### publicdomainvectors.org — Landscape Design Symbols
- **URL**: https://publicdomainvectors.org/en/free-vector-landscape-design-symbols
- **Format**: SVG, AI, EPS (not DXF/DWG — requires conversion)
- **License**: Public domain (no restrictions, including commercial)
- **Contents**: 7,212+ landscape vectors including plan-view trees ("hand drawn doodle top view trees for landscape plan")
- **Relevance**: Moderate — SVG requires conversion to DXF for LibreCAD; but public domain status makes these ideal for building a custom symbol library. LibreCAD can import SVG.
- **Conversion**: LibreCAD supports SVG import natively (File > Import > SVG). Alternatively use Inkscape to export as DXF.

---

### 3C. Summary Comparison Table

| Source | Format | Plan View | Palms | Cacti/Succulents | Groundcover | License | Best For |
|--------|--------|-----------|-------|-----------------|-------------|---------|----------|
| growdigital/blocks-forestgarden | DXF | Yes | No | No | No | Check repo | Open-source, LibreCAD-native |
| GSStnb/dxfBlocks | DXF | Partial | Unknown | Unknown | Unknown | CC BY-NC-SA 4.0 | LibreCAD blocks |
| dwgshare.com | DWG | Yes | Unknown | No | Unknown | Verify | Large plan-view tree library |
| cad-blocks.net | DWG | Yes (437) | Yes | No | Yes | Free | Largest general collection |
| cadblocksdwg.com | DWG | Yes | Yes | Yes | Yes | Free | Southern California relevance |
| freecads.com | DWG/DXF | Yes | Unknown | Unknown | Unknown | Free/Premium | Multi-format flexibility |
| firstinarchitecture.co.uk | DWG | Yes | No | No | Yes | Free (no resell) | Shrubs and groundcover |
| pincad.com | DWG | Yes | No | No | No | Free | Succulents |
| cadblocksforfree.com | DWG | No (elevation) | No | Yes | No | Free | Cacti symbols |
| linecad.com | DWG | Yes | Yes | No | Yes | Verify | Comprehensive multi-type |
| publicdomainvectors.org | SVG | Yes | No | No | No | Public Domain | Building custom library |

---

## 4. Plant Databases

### 4A. WUCOLS V (Primary Recommendation)

- **Full name**: Water Use Classification of Landscape Species
- **URL**: https://wucols.ucdavis.edu/
- **Maintained by**: California Center for Urban Horticulture (CCUH), UC Davis
- **Download**: https://ccuh.ucdavis.edu/wucols-db — full database downloadable as XLSX (convertible to CSV)
- **Current version**: WUCOLS V (live March 25, 2025)
- **Plant count**: 4,100+ taxa
- **Format**: XLSX download, web search interface at wucols.ucdavis.edu/plant-search-database
- **Data fields include**:
  - Botanical name
  - Common name
  - Water use rating per California climate region (Very Low / Low / Moderate / High)
  - 6 California climate regions covered
- **License**: UC Davis academic resource — free for professional use
- **Relevance**: CRITICAL — WUCOLS is the official California water budget tool. Ojai falls in Region 3 (South Coast) or Region 4 (Central Valley fringe). Water budgets for landscape plans in most California jurisdictions reference WUCOLS ratings.
- **How to use**: Download XLSX from ccuh.ucdavis.edu/wucols-db, filter by Region 3 (South Coast), export plant subset as CSV for import into Netrun CAD plant database.

**Note on WUCOLS IV**: The prior edition (2014) covered 3,500+ taxa. WUCOLS V is the current standard. The UC Davis download page (ucanr.edu/sites/WUCOLS/Download_WUCOLS_IV_List/) for the older edition returned 404 — use WUCOLS V exclusively.

---

### 4B. USDA PLANTS Database

- **URL**: https://plants.usda.gov/
- **GBIF mirror**: https://www.gbif.org/dataset/705922f7-5ba5-49ab-a75d-722e3090e690
- **API**: Official USDA PLANTS Web API — R wrapper available at https://mikemahoney218.github.io/plantr/
- **Data fields**:
  - Botanical name (accepted nomenclature), USDA symbol
  - Common names
  - Growth habit, duration
  - Native/introduced status by state (California native flag)
  - Noxious/invasive status
  - Distribution by state and county
- **Missing from API**: USDA hardiness zone is not a PLANTS database field (that data comes from USDA ARS separately)
- **Download**: Full state plant list downloadable as CSV from plants.usda.gov — select state "California", check "Download" button
- **License**: US government public domain
- **Relevance**: High for confirming California native status and botanical name authority

---

### 4C. Calscape (California Native Plant Society)

- **URL**: https://calscape.org/
- **Maintained by**: California Native Plant Society (CNPS)
- **Data fields** (via web interface):
  - Common name, botanical name
  - Water needs (Very Low / Low / Moderate / High)
  - Sun exposure (Full Sun / Part Shade / Full Shade)
  - Soil type preferences
  - Bloom season and color
  - Height range
  - Wildlife value (pollinators, birds)
  - Location-specific results (enter address to get plants native to your area)
- **API**: No public API documented. Data not bulk-downloadable.
- **How to use**: Use web interface at calscape.org/search — enter Ojai, CA address to get plants native specifically to Ventura County / Ojai Valley. Manual export of search results.
- **License**: Data from Jepson eFlora and nearly 2 million verified field observations — academic use permissible
- **Relevance**: Very High — location-aware native plant search tailored to Ojai Valley

---

### 4D. Theodore Payne Foundation — California Native Plant Database

- **URL**: https://theodorepayne.org/nativeplantdatabase/
- **Focus**: Southern California native plants specifically
- **Data fields**: Botanical name, common name, family, plant type (tree/shrub/groundcover/grass/bulb/fern), water needs, flower color
- **Browse by**: Plant type, flower color, water needs, special garden purposes
- **Download**: No bulk download available — web browsing only
- **Relevance**: High — Southern California focus aligns with Ojai geography

---

### 4E. CalFlora

- **URL**: https://www.calflora.org/
- **Contents**: 3.1+ million plant observations, 8,000+ taxa statewide
- **Download**: CSV and tab-delimited exports from search results (first 750 records per query)
- **Data fields**: Botanical name, common name, observation location (lat/lon), habitat, rare status
- **Note**: CalFlora is primarily an occurrence database (where plants are found in the wild), not a horticultural database. Less useful for water use or landscape size data.
- **Relevance**: Moderate — use to verify which native species actually occur in Ventura County

---

### 4F. Las Pilitas Nursery — Native Plant Database

- **URL**: https://www.laspilitas.com/plants/plants.htm
- **Contents**: 2,000+ pages of California native plant information — 350+ species in active nursery inventory
- **Data available**: Scientific name, common name, height, width, water use, sun exposure, wildlife value, fire resistance, deer resistance, soil requirements, ecological community
- **Specialties**: 50+ Manzanita varieties, extensive native grass and groundcover information
- **Download**: No bulk download — web browsing; "Printable availability list" for Santa Margarita location
- **Relevance**: Very High — most comprehensive California native horticultural data; ecologically organized by plant community

---

## 5. Recommended Download Priority for Netrun CAD

### Immediate Downloads (This Week)

1. **WUCOLS V plant list** (XLSX from ccuh.ucdavis.edu/wucols-db) — master water use reference
2. **growdigital/blocks-forestgarden** (git clone) — DXF blocks, LibreCAD-native
3. **cadblocksdwg.com landscape collection** — includes palms and cacti
4. **pincad.com succulents DWG** — for succulent groundcover and accent plant symbols
5. **firstinarchitecture.co.uk shrubs and groundcover** — DWG shrub symbols

### Secondary (Next Sprint)

6. **cad-blocks.net vegetation blocks** — large plan-view tree library
7. **publicdomainvectors.org** — SVG conversions to build custom symbol DXF
8. **USDA PLANTS California CSV** — botanical name authority and native status

---

## 6. Information Gaps

- No open-source DXF library was found specifically for California native plants (Toyon, Manzanita, Salvia, Ceanothus, etc.) — these will need to be drawn as custom blocks.
- WUCOLS uses its own climate regions (1-6), not identical to USDA hardiness zones. Zone 9b covers parts of WUCOLS Regions 3 (South Coast) and 4 (Central Valley). Verify Ojai's WUCOLS region on the wucols.ucdavis.edu map.
- Most free DWG blocks do not have explicit commercial use licenses. Confirm with each source before including in deliverable drawings billed to clients.
- No single source covers all: symbols + water use + California native + size data simultaneously. A custom database join will be required.

---

## 7. Recommended Architecture: Netrun CAD Plant Database

The plant database CSV (see `landscape/data/plant_database_ojai_zone9b_v1.0.csv`) uses this schema:

```
common_name, botanical_name, family, usda_zone_min, usda_zone_max, water_use,
sun_exposure, mature_height_ft, mature_spread_ft, native_to_california,
drought_tolerant, deer_resistant, fire_resistant, symbol_file
```

**Water use values** follow WUCOLS convention: `VL` (Very Low), `L` (Low), `M` (Moderate), `H` (High)
**Sun exposure values**: `FS` (Full Sun), `PS` (Part Shade), `SH` (Full Shade), `FS/PS` (tolerates both)

---

## Micro-Retrospective

### What Went Well
1. Found multiple free DXF/DWG sources covering all required plant types (trees, shrubs, groundcover, palms, cacti, succulents)
2. Identified WUCOLS V as the authoritative, downloadable California water use database — exactly what landscape professionals need for permit documentation
3. Confirmed LibreCAD's SVG import capability opens public domain SVG sources as an additional supply

### What Needs Improvement
1. Several official sites (WUCOLS download page, ccuh.ucdavis.edu) returned 403 errors — need to access these manually in a browser session
2. No open-source symbol library exists specifically for California native plants — this is a gap Netrun CAD could fill uniquely

### Action Items
1. **Manual download session**: Allie should open WUCOLS V XLSX at ccuh.ucdavis.edu/wucols-db in a browser (the UC Davis server blocks automated fetch) — save as CSV for import
2. **Custom symbol priority list**: Based on 50-plant database, identify the 15 highest-frequency species and create custom DXF plan-view blocks as the first Netrun CAD contribution

### Patterns Discovered
- **Pattern**: Government horticultural databases (WUCOLS, USDA PLANTS) block automated scrapers but offer full XLSX/CSV downloads via browser — always direct users to manual download for these sources
- **Anti-Pattern**: Assuming DWG "free download" implies commercial use rights — most sites are silent on this; CC-licensed sources (dxfBlocks) are more legally clear even with restrictions
