/*****************************************************************************/
/*  irrigation.cpp - Irrigation planning plugin for Netrun CAD              */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*****************************************************************************/

#include "irrigation.h"
#include "document_interface.h"

#include <QComboBox>
#include <QDoubleSpinBox>
#include <QFormLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QMessageBox>
#include <QPushButton>
#include <QSpinBox>
#include <QVBoxLayout>
#include <QDebug>

// Default coverage radii by head type (feet)
static double defaultRadius(const QString &type)
{
    if (type.contains("Rotor"))    return 15.0;
    if (type.contains("Spray"))    return  8.0;
    if (type.contains("Drip"))     return  1.5;
    if (type.contains("Bubbler"))  return  2.0;
    return 8.0;
}

static double defaultGPM(const QString &type)
{
    if (type.contains("Rotor"))    return 2.5;
    if (type.contains("Spray"))    return 1.5;
    if (type.contains("Drip"))     return 0.5;
    if (type.contains("Bubbler"))  return 1.0;
    return 1.5;
}

// ---------------------------------------------------------------------------
// IrrigationPlugin
// ---------------------------------------------------------------------------

QString IrrigationPlugin::name() const
{
    return tr("Irrigation Planning");
}

PluginCapabilities IrrigationPlugin::getCapabilities() const
{
    PluginCapabilities caps;
    caps.menuEntryPoints
        << PluginMenuLocation("plugins_menu",
                              tr("Irrigation - Place Head..."),
                              tr("Place a sprinkler or drip head with coverage circle"))
        << PluginMenuLocation("plugins_menu",
                              tr("Irrigation - Coverage Report"),
                              tr("Summarize GPM and coverage for current drawing"));
    return caps;
}

void IrrigationPlugin::execComm(Document_Interface *doc, QWidget *parent, QString cmd)
{
    if (cmd == "coverage") {
        showCoverageReport(doc, parent);
    } else {
        placeHead(doc, parent);
    }
}

void IrrigationPlugin::placeHead(Document_Interface *doc, QWidget *parent)
{
    IrrigationHeadDialog dlg(parent);
    if (dlg.exec() != QDialog::Accepted)
        return;

    QString headType = dlg.headType();
    double  radius   = dlg.coverageRadius();
    double  gpm      = dlg.gpm();
    int     zone     = dlg.zone();

    // Phase 1: stub — log head placement intent.
    // Phase 2:
    //   1. Prompt user to click a point on the drawing (via Document_Interface pick)
    //   2. Insert head symbol block at that point on layer "IRRIGATION-HEADS-Z{zone}"
    //   3. Draw coverage circle (doc->addCircle) on layer "IRRIGATION-COVERAGE-Z{zone}"
    qDebug() << "[Irrigation] Place" << headType
             << "r=" << radius << "GPM=" << gpm << "Zone=" << zone;
    Q_UNUSED(doc)

    QMessageBox::information(parent, tr("Irrigation Planning"),
        tr("Irrigation plugin loaded (phase 1 stub).\n\n"
           "Head type: %1\nCoverage radius: %2 ft\nGPM: %3\nZone: %4\n\n"
           "Click-to-place and coverage circles are planned for phase 2.")
        .arg(headType)
        .arg(radius)
        .arg(gpm)
        .arg(zone));
}

void IrrigationPlugin::showCoverageReport(Document_Interface *doc, QWidget *parent)
{
    // Phase 1: stub.
    // Phase 2: count irrigation head blocks by zone layer, sum GPM, report gaps.
    qDebug() << "[Irrigation] Coverage report requested.";
    Q_UNUSED(doc)

    QMessageBox::information(parent, tr("Coverage Report"),
        tr("Coverage report generation is planned for phase 2.\n\n"
           "It will scan irrigation head blocks, sum GPM by zone, "
           "and flag areas with insufficient coverage."));
}


// ---------------------------------------------------------------------------
// IrrigationHeadDialog
// ---------------------------------------------------------------------------

IrrigationHeadDialog::IrrigationHeadDialog(QWidget *parent)
    : QDialog(parent)
{
    setWindowTitle(tr("Place Irrigation Head"));
    setMinimumWidth(360);

    auto *layout = new QFormLayout(this);

    headTypeCombo = new QComboBox(this);
    headTypeCombo->addItems({
        tr("Rotor Head (15 ft radius)"),
        tr("Spray Head (8 ft radius)"),
        tr("Drip Emitter (1.5 ft radius)"),
        tr("Bubbler (2 ft radius)")
    });
    layout->addRow(tr("Head type:"), headTypeCombo);

    radiusSpinBox = new QDoubleSpinBox(this);
    radiusSpinBox->setRange(0.5, 100.0);
    radiusSpinBox->setValue(8.0);
    radiusSpinBox->setSuffix(tr(" ft"));
    radiusSpinBox->setDecimals(1);
    layout->addRow(tr("Coverage radius:"), radiusSpinBox);

    gpmSpinBox = new QDoubleSpinBox(this);
    gpmSpinBox->setRange(0.1, 20.0);
    gpmSpinBox->setValue(1.5);
    gpmSpinBox->setSuffix(tr(" GPM"));
    gpmSpinBox->setDecimals(2);
    layout->addRow(tr("Flow rate:"), gpmSpinBox);

    zoneSpinBox = new QSpinBox(this);
    zoneSpinBox->setRange(1, 20);
    zoneSpinBox->setValue(1);
    zoneSpinBox->setPrefix(tr("Zone "));
    layout->addRow(tr("Irrigation zone:"), zoneSpinBox);

    auto *buttonRow = new QHBoxLayout;
    auto *acceptBtn = new QPushButton(tr("Place Head"), this);
    auto *cancelBtn = new QPushButton(tr("Cancel"), this);
    buttonRow->addStretch();
    buttonRow->addWidget(acceptBtn);
    buttonRow->addWidget(cancelBtn);
    layout->addRow(buttonRow);

    connect(headTypeCombo, QOverload<int>::of(&QComboBox::currentIndexChanged),
            this, &IrrigationHeadDialog::onHeadTypeChanged);
    connect(acceptBtn, &QPushButton::clicked, this, &IrrigationHeadDialog::checkAccept);
    connect(cancelBtn, &QPushButton::clicked, this, &QDialog::reject);
}

IrrigationHeadDialog::~IrrigationHeadDialog() = default;

QString IrrigationHeadDialog::headType() const        { return headTypeCombo->currentText(); }
double  IrrigationHeadDialog::coverageRadius() const  { return radiusSpinBox->value(); }
double  IrrigationHeadDialog::gpm() const             { return gpmSpinBox->value(); }
int     IrrigationHeadDialog::zone() const            { return zoneSpinBox->value(); }

void IrrigationHeadDialog::onHeadTypeChanged(int /*index*/)
{
    QString type = headTypeCombo->currentText();
    radiusSpinBox->setValue(defaultRadius(type));
    gpmSpinBox->setValue(defaultGPM(type));
}

void IrrigationHeadDialog::checkAccept()
{
    accept();
}
