/*****************************************************************************/
/*  plant_database.h - Plant catalog plugin for Netrun CAD                  */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*                                                                           */
/*  Searchable plant catalog backed by SQLite. Plants are inserted as        */
/*  LibreCAD block references at a chosen location. Generates a planting    */
/*  schedule table from entities on the drawing.                             */
/*                                                                           */
/*  This library is free software; you can redistribute it and/or modify    */
/*  it under the terms of the GNU General Public License as published by     */
/*  the Free Software Foundation; either version 2 of the License, or       */
/*  (at your option) any later version.                                      */
/*****************************************************************************/

#ifndef PLANT_DATABASE_H
#define PLANT_DATABASE_H

#include "qc_plugininterface.h"
#include <QDialog>
#include <QObject>

class QLineEdit;
class QListWidget;
class QLabel;

/**
 * Plant Database plugin — browse the plant catalog and insert plant symbols.
 *
 * Phase 1 (current): UI stub with hardcoded sample plants.
 * Phase 2: Wire in SQLite DB with full USDA plant data, zone filtering,
 *           water-use categories, and planting schedule export.
 */
class PlantDatabasePlugin : public QObject, public QC_PluginInterface
{
    Q_OBJECT
    Q_INTERFACES(QC_PluginInterface)
    Q_PLUGIN_METADATA(IID LC_DocumentInterface_iid FILE "plant_database.json")

public:
    QString name() const override;
    PluginCapabilities getCapabilities() const override;
    void execComm(Document_Interface *doc, QWidget *parent, QString cmd) override;

private:
    void showPlantBrowser(Document_Interface *doc, QWidget *parent);
    void generatePlantingSchedule(Document_Interface *doc, QWidget *parent);
};


/**
 * Plant browser dialog — search and insert plant symbols.
 */
class PlantBrowserDialog : public QDialog
{
    Q_OBJECT

public:
    explicit PlantBrowserDialog(QWidget *parent = nullptr);
    ~PlantBrowserDialog() override;

    QString selectedPlant() const;

public slots:
    void filterPlants(const QString &text);
    void checkAccept();

private:
    void populatePlants(const QString &filter = QString());

    QLineEdit   *searchEdit;
    QListWidget *plantList;
    QLabel      *detailLabel;
};

#endif // PLANT_DATABASE_H
