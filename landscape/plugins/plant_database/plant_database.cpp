/*****************************************************************************/
/*  plant_database.cpp - Plant catalog plugin for Netrun CAD                */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*****************************************************************************/

#include "plant_database.h"
#include "document_interface.h"

#include <QGridLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QListWidget>
#include <QMessageBox>
#include <QPushButton>
#include <QVBoxLayout>
#include <QDebug>

// Phase 1: hardcoded sample plant catalog.
// Phase 2: replace with SQLite query from landscape/plugins/plant_database/resources/plants.db
static const QStringList SAMPLE_PLANTS = {
    "Agapanthus africanus | African Lily | Zone 9-11 | Low water",
    "Achillea millefolium | Common Yarrow | Zone 3-9 | Low water",
    "Salvia leucantha | Mexican Bush Sage | Zone 8-11 | Low water",
    "Lantana camara | Lantana | Zone 8-11 | Low water",
    "Lavandula angustifolia | English Lavender | Zone 5-8 | Low water",
    "Rosmarinus officinalis | Rosemary | Zone 7-10 | Low water",
    "Cercis occidentalis | Western Redbud | Zone 7-9 | Low water",
    "Muhlenbergia rigens | Deer Grass | Zone 7-10 | Low water",
    "Festuca glauca | Blue Fescue | Zone 4-8 | Low water",
    "Arctostaphylos | Manzanita | Zone 6-10 | Low water",
};

// ---------------------------------------------------------------------------
// PlantDatabasePlugin
// ---------------------------------------------------------------------------

QString PlantDatabasePlugin::name() const
{
    return tr("Plant Database");
}

PluginCapabilities PlantDatabasePlugin::getCapabilities() const
{
    PluginCapabilities caps;
    caps.menuEntryPoints
        << PluginMenuLocation("plugins_menu",
                              tr("Plant Database - Browse..."),
                              tr("Search plant catalog and insert plant symbols"))
        << PluginMenuLocation("plugins_menu",
                              tr("Plant Database - Planting Schedule"),
                              tr("Generate planting schedule from current drawing"));
    return caps;
}

void PlantDatabasePlugin::execComm(Document_Interface *doc, QWidget *parent, QString cmd)
{
    if (cmd == "plantschedule") {
        generatePlantingSchedule(doc, parent);
    } else {
        showPlantBrowser(doc, parent);
    }
}

void PlantDatabasePlugin::showPlantBrowser(Document_Interface *doc, QWidget *parent)
{
    PlantBrowserDialog dlg(parent);
    if (dlg.exec() != QDialog::Accepted)
        return;

    QString plant = dlg.selectedPlant();

    // Phase 1: stub — log selection.
    // Phase 2: insert plant block reference at user-picked location via doc->insertBlock().
    qDebug() << "[Plant Database] Selected plant:" << plant;
    Q_UNUSED(doc)

    QMessageBox::information(parent, tr("Plant Database"),
        tr("Plant Database plugin loaded (phase 1 stub).\n\n"
           "Selected: %1\n\n"
           "Block insertion is planned for phase 2.").arg(plant));
}

void PlantDatabasePlugin::generatePlantingSchedule(Document_Interface *doc, QWidget *parent)
{
    // Phase 1: stub.
    // Phase 2: scan drawing blocks with plant metadata attributes,
    //          count by species, write a schedule table.
    qDebug() << "[Plant Database] Planting schedule requested.";
    Q_UNUSED(doc)

    QMessageBox::information(parent, tr("Planting Schedule"),
        tr("Planting schedule generation is planned for phase 2.\n\n"
           "It will scan the drawing for plant block references and "
           "produce a count-by-species table."));
}


// ---------------------------------------------------------------------------
// PlantBrowserDialog
// ---------------------------------------------------------------------------

PlantBrowserDialog::PlantBrowserDialog(QWidget *parent)
    : QDialog(parent)
{
    setWindowTitle(tr("Plant Database"));
    setMinimumSize(480, 360);

    auto *layout = new QVBoxLayout(this);

    layout->addWidget(new QLabel(tr("Search:")));
    searchEdit = new QLineEdit(this);
    searchEdit->setPlaceholderText(tr("Type plant name or zone..."));
    layout->addWidget(searchEdit);

    plantList = new QListWidget(this);
    plantList->setAlternatingRowColors(true);
    layout->addWidget(plantList);

    detailLabel = new QLabel(tr("Select a plant to see details."), this);
    detailLabel->setWordWrap(true);
    layout->addWidget(detailLabel);

    auto *buttonRow = new QHBoxLayout;
    auto *insertBtn = new QPushButton(tr("Insert Symbol"), this);
    auto *cancelBtn = new QPushButton(tr("Cancel"), this);
    buttonRow->addStretch();
    buttonRow->addWidget(insertBtn);
    buttonRow->addWidget(cancelBtn);
    layout->addLayout(buttonRow);

    populatePlants();

    connect(searchEdit, &QLineEdit::textChanged, this, &PlantBrowserDialog::filterPlants);
    connect(insertBtn,  &QPushButton::clicked,   this, &PlantBrowserDialog::checkAccept);
    connect(cancelBtn,  &QPushButton::clicked,   this, &QDialog::reject);
    connect(plantList,  &QListWidget::currentTextChanged, detailLabel, &QLabel::setText);
}

PlantBrowserDialog::~PlantBrowserDialog() = default;

QString PlantBrowserDialog::selectedPlant() const
{
    auto *item = plantList->currentItem();
    return item ? item->text() : QString();
}

void PlantBrowserDialog::filterPlants(const QString &text)
{
    populatePlants(text);
}

void PlantBrowserDialog::populatePlants(const QString &filter)
{
    plantList->clear();
    for (const QString &entry : SAMPLE_PLANTS) {
        if (filter.isEmpty() || entry.contains(filter, Qt::CaseInsensitive))
            plantList->addItem(entry);
    }
}

void PlantBrowserDialog::checkAccept()
{
    if (!plantList->currentItem()) {
        QMessageBox::warning(this, tr("Plant Database"), tr("Please select a plant."));
        return;
    }
    accept();
}
