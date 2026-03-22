/*****************************************************************************/
/*  gis_import.cpp - GIS file import plugin for Netrun CAD                  */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*****************************************************************************/

#include "gis_import.h"
#include "document_interface.h"

#include <QComboBox>
#include <QFileDialog>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QMessageBox>
#include <QPushButton>
#include <QDebug>

// ---------------------------------------------------------------------------
// GISImportPlugin
// ---------------------------------------------------------------------------

QString GISImportPlugin::name() const
{
    return tr("GIS Import");
}

PluginCapabilities GISImportPlugin::getCapabilities() const
{
    PluginCapabilities caps;
    caps.menuEntryPoints
        << PluginMenuLocation("plugins_menu",
                              tr("GIS Import..."),
                              tr("Import GeoTIFF, Shapefile, or KML/KMZ into drawing"));
    return caps;
}

void GISImportPlugin::execComm(Document_Interface *doc, QWidget *parent, QString cmd)
{
    Q_UNUSED(cmd)

    GISImportDialog dlg(parent);
    if (dlg.exec() != QDialog::Accepted)
        return;

    QString filePath = dlg.selectedFile();
    QString format   = dlg.selectedFormat();

    // Phase 1: stub — log intent, show placeholder message.
    // Phase 2: call GDAL/OGR here to parse features and call doc->addLine() etc.
    qDebug() << "[GIS Import] Plugin loaded. File:" << filePath << "Format:" << format;
    Q_UNUSED(doc)

    QMessageBox::information(parent, tr("GIS Import"),
        tr("GIS Import plugin loaded (phase 1 stub).\n\n"
           "Selected: %1\nFormat: %2\n\n"
           "GDAL/OGR integration is planned for phase 2.")
        .arg(filePath, format));
}


// ---------------------------------------------------------------------------
// GISImportDialog
// ---------------------------------------------------------------------------

GISImportDialog::GISImportDialog(QWidget *parent)
    : QDialog(parent)
{
    setWindowTitle(tr("GIS Import"));
    setMinimumWidth(420);

    auto *layout = new QGridLayout(this);

    layout->addWidget(new QLabel(tr("File:")), 0, 0);
    filePathEdit = new QLineEdit(this);
    filePathEdit->setPlaceholderText(tr("Select a GeoTIFF, .shp, or .kml file..."));
    layout->addWidget(filePathEdit, 0, 1);

    browseButton = new QPushButton(tr("Browse..."), this);
    layout->addWidget(browseButton, 0, 2);

    layout->addWidget(new QLabel(tr("Format:")), 1, 0);
    formatCombo = new QComboBox(this);
    formatCombo->addItems({tr("Auto-detect"), "GeoTIFF", "Shapefile (.shp)", "KML/KMZ"});
    layout->addWidget(formatCombo, 1, 1, 1, 2);

    auto *buttonRow = new QHBoxLayout;
    acceptButton = new QPushButton(tr("Import"), this);
    cancelButton = new QPushButton(tr("Cancel"), this);
    buttonRow->addStretch();
    buttonRow->addWidget(acceptButton);
    buttonRow->addWidget(cancelButton);
    layout->addLayout(buttonRow, 2, 0, 1, 3);

    connect(browseButton, &QPushButton::clicked, this, &GISImportDialog::browseFile);
    connect(acceptButton, &QPushButton::clicked, this, &GISImportDialog::checkAccept);
    connect(cancelButton, &QPushButton::clicked, this, &QDialog::reject);
}

GISImportDialog::~GISImportDialog() = default;

QString GISImportDialog::selectedFile() const
{
    return filePathEdit->text();
}

QString GISImportDialog::selectedFormat() const
{
    return formatCombo->currentText();
}

void GISImportDialog::browseFile()
{
    QString path = QFileDialog::getOpenFileName(
        this, tr("Select GIS File"), QString(),
        tr("GIS Files (*.tif *.tiff *.shp *.kml *.kmz);;All Files (*)"));
    if (!path.isEmpty())
        filePathEdit->setText(path);
}

void GISImportDialog::checkAccept()
{
    if (filePathEdit->text().trimmed().isEmpty()) {
        QMessageBox::warning(this, tr("GIS Import"), tr("Please select a file to import."));
        return;
    }
    accept();
}
