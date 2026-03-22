# Netrun CAD — Getting Started Guide for Allie

Hey Allie! This is your guide to the new landscape design tools Daniel built for you. There are two apps — pick whichever fits what you're doing.

---

## Which App Should I Use?

**Netrun CAD Web** (iPad + Apple Pencil) — `cad.netrunsystems.com`
Use this when you want to:
- Sketch planting plans with your Apple Pencil
- Hand-color a plan with watercolor brushes
- Add your handwriting to labels and notes
- Work from the couch, the shop, or a client's site
- Pull up a satellite view of a property to trace over
- Save projects to Google Drive and share with clients

**Netrun CAD Desktop** (Windows, on your Dell)
Use this when you need:
- Precise measurements and dimensioning
- DWG files for contractors
- Complex editing with snap-to-grid
- Large DXF files with many layers

You can go back and forth — both apps read and write DXF files.

---

## The iPad App (Netrun CAD Web)

### Opening It
Open Safari on your iPad and go to **cad.netrunsystems.com**

### The 4 Modes (switch with the buttons at the top)

**1. CAD Mode** (ruler icon) — key: `1`
For precise drawing — lines, rectangles, circles. Tap two points to draw a line. The measurement shows automatically in feet and inches. Grid snapping keeps everything aligned.

**2. Draw Mode** (pencil icon) — key: `2` — YOUR FAVORITE
This is where the Apple Pencil shines. Pick a pen size and color, then draw directly on the plan. Press harder for thicker lines, lighter for thin. It feels like drawing on paper.

Use this for:
- Sketching planting areas
- Drawing tree canopies freehand
- Adding organic shapes that CAD mode can't do
- Quick concept sketches with a client watching

**3. Color Mode** (paintbrush icon) — key: `3`
Watercolor and marker brushes. Press lightly for transparent washes, harder for opaque fills. The color palette has landscape greens, browns, and blues ready to go.

Use this for:
- Coloring planting areas (green washes for shrub beds)
- Shading hardscape (gray for concrete, tan for DG)
- The hand-colored look your clients love — without printing and re-scanning

**4. Text Mode** (T icon) — key: `4`
Type text and tap where you want it on the plan. The font looks like architect's handwriting.

---

### Layers
The layer panel (right side, click "Layers" button) controls what's visible:
- **Site** — property lines, structures, existing trees
- **Hardscape** — paths, patios, walls, DG areas
- **Planting** — all your plant placements
- **Irrigation** — drip lines, spray heads
- **Drawing** — your Apple Pencil sketches
- **Color** — your watercolor fills
- **Text** — labels and notes
- **GIS** — satellite basemap and property data
- **Scan** — KIRI 3D scan data

Toggle the eye icon to show/hide each layer. Lock a layer (padlock) so you don't accidentally draw on it.

---

### Satellite Basemap
Tap **Basemap** at the top. Type in the project address. A satellite view loads behind your drawing — now you can trace the property, see existing trees, and understand the site without being there.

Pinch to zoom, two fingers to pan.

---

### Command Line
At the very bottom of the screen is a command line — just like AutoCAD.

You can type any command or shortcut and press Enter:
- `L` → Line
- `C` → Circle
- `R` → Rectangle
- `D` → Dimension
- `PLANT` → Open plant browser
- `BASEMAP` → Toggle satellite view
- `SCAN` → Import a KIRI scan
- `SAVE` / `OPEN` → Project management
- `?` → Show all commands

The command line accepts all 88 standard AutoCAD LT shortcut aliases. If you know an AutoCAD shortcut, it probably works here.

**How it works:**
- Type a command (or just press a letter key — the command line opens automatically, just like AutoCAD)
- Press **Enter** to run it
- Press **Tab** for suggestions
- Press **Escape** to cancel
- Press **Enter** again (with nothing typed) to repeat the last command

---

### Right-Click Context Menu
Right-click (or long-press on iPad) anywhere on the canvas for quick options:
- Repeat last command
- Undo / Redo
- Pan / Zoom controls
- Delete last element

---

### Status Bar
The bar at the very bottom (below the command line) shows:
- Current **mode** and **tool**
- Whether **grid** and **snap** are on
- Your **cursor position** in feet (X, Y)
- Current **zoom** level
- Total **element count**
- Buttons: **Clear All** and **Reset View**

---

### Help & Reference Panel
Click the **?** button (top right) or press the **?** key anytime to open the help panel.

Inside you'll find:
- **Quick Start** — mode overview, first line walkthrough
- **Keyboard Shortcuts** — all 88 AutoCAD aliases organized by category
- **Tools Reference** — what each tool does in each mode
- **Plant Database Guide** — water ratings, icons explained
- **Import/Export** — DXF, PDF, GIS, KIRI, Google Drive explained
- **About** — version, credits, license

There's a search bar at the top of the help panel — type anything to find it.

---

### Importing a Site Scan
If you scanned the site with KIRI Engine on your iPhone:
1. Export the scan as an OBJ file from KIRI
2. In Netrun CAD Web, tap **Import 3D Scan** (in the ImportExport toolbar)
3. Select the OBJ file
4. The app projects the 3D scan to a flat plan view
5. It automatically finds the site boundary and draws contour lines
6. Now you have a base to design on

PLY files from KIRI also work.

---

### Plants
The plant panel (click "Plants" or type `PLANT`) has California natives and drought-tolerant species with:
- Water use ratings (VL=Very Low / L=Low / M=Moderate / H=High), from WUCOLS IV
- Sun requirements
- Mature size
- Deer and fire resistance

Tap a plant to select it, then tap the canvas to place it. The symbol appears at the right scale. Tap the same plant again to stop placing.

---

### Saving Your Work

**Auto-save to browser**: Your drawing saves locally every 5 seconds automatically. Even if you close the tab and reopen it, your last drawing is still there.

**Google Drive**: Click the **Drive** button in the project bar (top center). Sign in once with your Google account. After that:
- **Save** — saves the project as a `.ncad` file in your Google Drive
- **Open** — pick any saved project from the list
- **Share** — copies a view-only link to your clipboard. Send it to a client or contractor and they can see your plan in the browser.
- **Auto-save** — when signed in, saves every 5 minutes automatically

**Export DXF**: Tap Export DXF to download a file you can open on your Dell in the desktop app (or send to a contractor).

**Export PDF**: Tap Export PDF, choose your scale (1/4" = 1' is standard for residential), pick ARCH D for a 24×36 print, and download. The PDF includes a title block with project name, date, and scale.

---

### Keyboard Shortcuts (if you have a keyboard attached)

| Key | Action |
|-----|--------|
| `1` | CAD Mode |
| `2` | Draw Mode |
| `3` | Color Mode |
| `4` | Text Mode |
| `?` | Open / close Help panel |
| `L` | Line tool (CAD mode) |
| `R` | Rectangle tool (CAD mode) |
| `C` | Circle tool (CAD mode) |
| `D` | Dimension tool (CAD mode) |
| `V` | Select/Pan tool |
| `G` | Toggle grid |
| `S` | Toggle snap |
| `F8` | Toggle ortho mode (horizontal/vertical only) |
| `Enter` | Open command line / repeat last command |
| `Escape` | Cancel |
| `Ctrl+Z` | Undo |
| `Ctrl+Shift+Z` | Redo |
| `Delete` | Remove last element |
| `Ctrl+0` | Reset view |

---

## The Desktop App (Netrun CAD Desktop)

> **Note**: For most design work, the web app at cad.netrunsystems.com is now the primary tool. It has full DXF import/export, so you can start on the iPad and finish details on the desktop. The desktop app is best for complex DXF/DWG work and production drafting.

### Installing It
Daniel will give you a zip file. Extract it and run **LibreCAD.exe**. No installer needed — it's portable.

### AutoCAD Shortcuts You Already Know
All your muscle memory works. Type these in the command line at the bottom:

| You Type | What Happens |
|----------|-------------|
| `L` | Line |
| `C` | Circle |
| `M` | Move |
| `CO` | Copy |
| `TR` | Trim |
| `O` | Offset |
| `MI` | Mirror |
| `RO` | Rotate |
| `SC` | Scale |
| `E` | Erase |
| `U` | Undo |
| `Z` | Zoom |
| `LA` | Layer dialog |
| `DI` | Distance/measure |

It's the same as AutoCAD LT. If a shortcut doesn't work, let Daniel know and we'll add it.

### Setting Up the Shortcuts
Copy the file `landscape\autocad_aliases.txt` to:
```
C:\Users\Allie\AppData\Roaming\LibreCAD\librecad.alias
```
(Daniel can help with this the first time.)

### Opening DXF Files
File → Open → select any .dxf file. Your old AutoCAD LT files should open fine.

### Layer Setup for a New Landscape Plan
When you start a new plan, set up these layers (or use the template):

| Layer | Color | What Goes Here |
|-------|-------|---------------|
| SITE-BOUNDARY | White | Property lines |
| HARDSCAPE | Gray | Paths, patios, walls |
| PLANTING-TREES | Dark Green | Tree locations |
| PLANTING-SHRUBS | Light Green | Shrub beds |
| IRRIGATION | Blue | Drip and spray lines |
| DIMENSIONS | Red | Measurements |
| TEXT | White | Labels |

---

## Your Typical Project Workflow

Here's how a project flows from start to finish:

### 1. Site Visit
- Walk the property with your phone
- Scan key areas with KIRI Engine (iPhone) — capture the whole yard if you can
- Take measurements (tape measure or laser)
- Note existing trees, boulders, utilities, slopes
- Take photos

### 2. Base Plan (iPad — web app)
- Open cad.netrunsystems.com on your iPad
- Type the address and turn on the satellite basemap
- Or import the KIRI scan (Import 3D Scan)
- Switch to CAD Mode (key: 1)
- Draw the property boundary
- Add existing structures (house, garage, fences)
- Mark existing trees and boulders
- Add hardscape — paths, patios, walls, DG areas
- Dimension everything with the D key

### 3. Planting Design (iPad — Apple Pencil time!)
- Switch to Draw Mode (key: 2)
- Sketch planting areas freehand — tree canopies, shrub masses, groundcover zones
- Open the Plants panel and place plants from the database
- Use the plant info for spacing and mature size
- Switch to Color Mode (key: 3) — wash in the greens, tans, and browns

### 4. Add Details
- Switch to Text Mode (key: 4) for plant labels and callouts
- Add plant schedule notes
- Add irrigation and construction notes

### 5. Deliver to Client
- Export PDF at 1/4" = 1' on ARCH D (24×36")
- Or share via Google Drive link — they can view it in the browser, no software needed
- Export DXF if the contractor needs a CAD file

---

## The Plant Database

The app includes California native and drought-tolerant plants that work in Ojai's climate (USDA Zone 9b). Every plant has:

- **Water Use** — from WUCOLS ratings (VL=Very Low, L=Low, M=Moderate, H=High)
- **Sun** — Full Sun, Part Shade, Shade
- **Mature Size** — so you know spacing
- **Native to California** — yes or no
- **Drought Tolerant** — for water-wise designs
- **Deer Resistant** — important for Ojai!
- **Fire Resistant** — for defensible space zones

### Your Go-To Ojai Plants (already in the database)

**Trees**: Coast Live Oak, Valley Oak, California Sycamore, Olive, Italian Cypress, Toyon, Desert Willow, California Fan Palm

**Shrubs**: Ceanothus (California Lilac), Manzanita, White Sage, Black Sage, Cleveland Sage, Lavender, Rosemary, Agave, Aloe, Lemonade Berry

**Groundcovers**: Dymondia, Dwarf Coyote Brush, Blue Fescue, Deer Grass, Yarrow, Creeping Sage, Red Fescue (no-mow lawn alternative)

**Hardscape**: Decomposed Granite, Flagstone, Permeable Pavers, Dry Creek Beds, Crushed Rock Mulch, Boulder Borders

---

## Quick Reference Card

| I want to... | Do this... |
|-------------|-----------|
| Start a new project | Open the web app, toggle Basemap, search the address |
| Import a site scan | Import 3D Scan → select OBJ/PLY from KIRI |
| Draw precise lines | Switch to CAD Mode (key: 1) |
| Sketch freehand | Switch to Draw Mode (key: 2) |
| Color a plan | Switch to Color Mode (key: 3) |
| Add labels | Switch to Text Mode (key: 4) |
| Open help | Press `?` or click the `?` button |
| Use a command | Just start typing — the command line opens |
| Undo a mistake | Ctrl+Z (or Cmd+Z on iPad keyboard) |
| Zoom in/out | Pinch with two fingers |
| Pan around | Two-finger drag |
| Save to Google Drive | Click Drive → Save |
| Share with a client | Click Drive → Share → copy the link |
| Export a DXF | ImportExport toolbar → Export DXF |
| Print a plan | Export PDF → choose 1/4" = 1' → ARCH D |
| Find a plant | Open Plant panel → search by name |
| Place a plant | Tap plant in panel → tap canvas where you want it |
| Hide a layer | Tap the eye icon next to the layer name |
| Right-click on iPad | Long-press (hold finger 0.6 seconds) |
| See cursor position | Look at the status bar (bottom of screen) |
| Use on my Dell | Open cad.netrunsystems.com in Edge, or use the desktop app |

---

## Need Help?

Press **?** anywhere in the app to open the built-in help panel. It has everything in one place.

Or tell Daniel. He built this for you and can fix or add anything. The plant database, the symbols, the shortcuts — everything can be customized to how you work.

You've got this. Your design skills haven't gone anywhere — now you have modern tools that match how you actually think and draw.

---

*Netrun CAD — Built with love by Daniel, for Allie*
*Netrun Systems, Ojai, California*
