/*****************************************************************************/
/*  kiri_import.h - KIRI Engine scan import plugin for Netrun CAD           */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*                                                                           */
/*  Imports OBJ/PLY point cloud exports from the KIRI Engine iOS app.       */
/*  Projects the 3D scan to a 2D plan view and generates a site boundary    */
/*  as a LibreCAD polyline.                                                  */
/*                                                                           */
/*  This library is free software; you can redistribute it and/or modify    */
/*  it under the terms of the GNU General Public License as published by     */
/*  the Free Software Foundation; either version 2 of the License, or       */
/*  (at your option) any later version.                                      */
/*****************************************************************************/

#ifndef KIRI_IMPORT_H
#define KIRI_IMPORT_H

#include "qc_plugininterface.h"
#include <QDialog>
#include <QObject>

class QLineEdit;
class QDoubleSpinBox;
class QCheckBox;

/**
 * KIRI Import plugin — imports 3D scans from KIRI Engine and projects to 2D.
 *
 * Phase 1 (current): UI stub — shows dialog, logs command.
 * Phase 2: Parse OBJ/PLY point clouds, flatten to Z=0, hull-trace site boundary.
 */
class KIRIImportPlugin : public QObject, public QC_PluginInterface
{
    Q_OBJECT
    Q_INTERFACES(QC_PluginInterface)
    Q_PLUGIN_METADATA(IID LC_DocumentInterface_iid FILE "kiri_import.json")

public:
    QString name() const override;
    PluginCapabilities getCapabilities() const override;
    void execComm(Document_Interface *doc, QWidget *parent, QString cmd) override;
};


/**
 * Dialog for KIRI scan import options.
 */
class KIRIImportDialog : public QDialog
{
    Q_OBJECT

public:
    explicit KIRIImportDialog(QWidget *parent = nullptr);
    ~KIRIImportDialog() override;

    QString selectedFile() const;
    double  scaleFactor() const;
    bool    generateBoundary() const;

public slots:
    void browseFile();
    void checkAccept();

private:
    QLineEdit      *filePathEdit;
    QDoubleSpinBox *scaleSpinBox;
    QCheckBox      *boundaryCheckBox;
};

#endif // KIRI_IMPORT_H
