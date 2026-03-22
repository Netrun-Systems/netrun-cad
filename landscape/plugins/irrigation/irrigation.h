/*****************************************************************************/
/*  irrigation.h - Irrigation planning plugin for Netrun CAD                */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*                                                                           */
/*  Sprinkler and drip head placement with coverage circle visualization.   */
/*  Calculates GPM per zone and flags overlap/gap areas.                    */
/*                                                                           */
/*  This library is free software; you can redistribute it and/or modify    */
/*  it under the terms of the GNU General Public License as published by     */
/*  the Free Software Foundation; either version 2 of the License, or       */
/*  (at your option) any later version.                                      */
/*****************************************************************************/

#ifndef IRRIGATION_H
#define IRRIGATION_H

#include "qc_plugininterface.h"
#include <QDialog>
#include <QObject>

class QComboBox;
class QDoubleSpinBox;
class QSpinBox;

/**
 * Irrigation Planning plugin — place sprinkler/drip heads and visualize coverage.
 *
 * Phase 1 (current): UI stub with head type and radius selection.
 * Phase 2: Insert head symbol block + coverage circle as LibreCAD entities;
 *           zone grouping by layer; GPM calculation report.
 */
class IrrigationPlugin : public QObject, public QC_PluginInterface
{
    Q_OBJECT
    Q_INTERFACES(QC_PluginInterface)
    Q_PLUGIN_METADATA(IID LC_DocumentInterface_iid FILE "irrigation.json")

public:
    QString name() const override;
    PluginCapabilities getCapabilities() const override;
    void execComm(Document_Interface *doc, QWidget *parent, QString cmd) override;

private:
    void placeHead(Document_Interface *doc, QWidget *parent);
    void showCoverageReport(Document_Interface *doc, QWidget *parent);
};


/**
 * Dialog for configuring a sprinkler or drip head before placement.
 */
class IrrigationHeadDialog : public QDialog
{
    Q_OBJECT

public:
    explicit IrrigationHeadDialog(QWidget *parent = nullptr);
    ~IrrigationHeadDialog() override;

    QString headType() const;
    double  coverageRadius() const;   // in drawing units (feet or metres)
    double  gpm() const;
    int     zone() const;

public slots:
    void onHeadTypeChanged(int index);
    void checkAccept();

private:
    QComboBox      *headTypeCombo;
    QDoubleSpinBox *radiusSpinBox;
    QDoubleSpinBox *gpmSpinBox;
    QSpinBox       *zoneSpinBox;
};

#endif // IRRIGATION_H
