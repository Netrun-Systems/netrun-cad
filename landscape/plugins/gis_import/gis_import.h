/*****************************************************************************/
/*  gis_import.h - GIS file import plugin for Netrun CAD                    */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*                                                                           */
/*  Imports GeoTIFF, Shapefiles (.shp), and KML/KMZ files as LibreCAD      */
/*  entities. Requires GDAL/OGR library for file parsing (planned).         */
/*                                                                           */
/*  This library is free software; you can redistribute it and/or modify    */
/*  it under the terms of the GNU General Public License as published by     */
/*  the Free Software Foundation; either version 2 of the License, or       */
/*  (at your option) any later version.                                      */
/*****************************************************************************/

#ifndef GIS_IMPORT_H
#define GIS_IMPORT_H

#include "qc_plugininterface.h"
#include <QDialog>
#include <QObject>

class QLineEdit;
class QComboBox;
class QPushButton;

/**
 * GIS Import plugin — imports GeoTIFF, Shapefile, KML/KMZ into the active drawing.
 *
 * Phase 1 (current): UI stub — shows dialog, logs command, no actual file parsing.
 * Phase 2: Wire in GDAL/OGR to convert GIS features to RS_Line / RS_Arc entities.
 */
class GISImportPlugin : public QObject, public QC_PluginInterface
{
    Q_OBJECT
    Q_INTERFACES(QC_PluginInterface)
    Q_PLUGIN_METADATA(IID LC_DocumentInterface_iid FILE "gis_import.json")

public:
    QString name() const override;
    PluginCapabilities getCapabilities() const override;
    void execComm(Document_Interface *doc, QWidget *parent, QString cmd) override;
};


/**
 * Dialog for selecting a GIS file to import.
 */
class GISImportDialog : public QDialog
{
    Q_OBJECT

public:
    explicit GISImportDialog(QWidget *parent = nullptr);
    ~GISImportDialog() override;

    QString selectedFile() const;
    QString selectedFormat() const;

public slots:
    void browseFile();
    void checkAccept();

private:
    QLineEdit   *filePathEdit;
    QComboBox   *formatCombo;
    QPushButton *browseButton;
    QPushButton *acceptButton;
    QPushButton *cancelButton;
};

#endif // GIS_IMPORT_H
