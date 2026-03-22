/*****************************************************************************/
/*  kiri_import.cpp - KIRI Engine scan import plugin for Netrun CAD         */
/*                                                                           */
/*  Copyright (C) 2026 Netrun Systems                                        */
/*****************************************************************************/

#include "kiri_import.h"
#include "document_interface.h"

#include <QCheckBox>
#include <QDoubleSpinBox>
#include <QFileDialog>
#include <QGridLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QMessageBox>
#include <QPushButton>
#include <QDebug>

// ---------------------------------------------------------------------------
// KIRIImportPlugin
// ---------------------------------------------------------------------------

QString KIRIImportPlugin::name() const
{
    return tr("KIRI Scan Import");
}

PluginCapabilities KIRIImportPlugin::getCapabilities() const
{
    PluginCapabilities caps;
    caps.menuEntryPoints
        << PluginMenuLocation("plugins_menu",
                              tr("KIRI Scan Import..."),
                              tr("Import 3D scan from KIRI Engine, projected to 2D plan view"));
    return caps;
}

void KIRIImportPlugin::execComm(Document_Interface *doc, QWidget *parent, QString cmd)
{
    Q_UNUSED(cmd)

    KIRIImportDialog dlg(parent);
    if (dlg.exec() != QDialog::Accepted)
        return;

    QString filePath  = dlg.selectedFile();
    double  scale     = dlg.scaleFactor();
    bool    boundary  = dlg.generateBoundary();

    // Phase 1: stub — log intent.
    // Phase 2: parse OBJ/PLY, project XY points, optionally compute convex hull for boundary.
    qDebug() << "[KIRI Import] Plugin loaded. File:" << filePath
             << "Scale:" << scale << "Boundary:" << boundary;
    Q_UNUSED(doc)

    QMessageBox::information(parent, tr("KIRI Scan Import"),
        tr("KIRI Import plugin loaded (phase 1 stub).\n\n"
           "Selected: %1\nScale: %2\nGenerate boundary: %3\n\n"
           "OBJ/PLY parsing is planned for phase 2.")
        .arg(filePath)
        .arg(scale)
        .arg(boundary ? tr("Yes") : tr("No")));
}


// ---------------------------------------------------------------------------
// KIRIImportDialog
// ---------------------------------------------------------------------------

KIRIImportDialog::KIRIImportDialog(QWidget *parent)
    : QDialog(parent)
{
    setWindowTitle(tr("KIRI Scan Import"));
    setMinimumWidth(420);

    auto *layout = new QGridLayout(this);

    layout->addWidget(new QLabel(tr("Scan file (.obj / .ply):")), 0, 0);
    filePathEdit = new QLineEdit(this);
    filePathEdit->setPlaceholderText(tr("Select KIRI Engine export file..."));
    layout->addWidget(filePathEdit, 0, 1);

    auto *browseBtn = new QPushButton(tr("Browse..."), this);
    layout->addWidget(browseBtn, 0, 2);

    layout->addWidget(new QLabel(tr("Scale factor:")), 1, 0);
    scaleSpinBox = new QDoubleSpinBox(this);
    scaleSpinBox->setRange(0.001, 1000.0);
    scaleSpinBox->setValue(1.0);
    scaleSpinBox->setDecimals(3);
    scaleSpinBox->setSuffix(tr(" (1.0 = metres)"));
    layout->addWidget(scaleSpinBox, 1, 1, 1, 2);

    boundaryCheckBox = new QCheckBox(tr("Auto-generate site boundary from scan hull"), this);
    boundaryCheckBox->setChecked(true);
    layout->addWidget(boundaryCheckBox, 2, 0, 1, 3);

    auto *buttonRow = new QHBoxLayout;
    auto *acceptBtn = new QPushButton(tr("Import"), this);
    auto *cancelBtn = new QPushButton(tr("Cancel"), this);
    buttonRow->addStretch();
    buttonRow->addWidget(acceptBtn);
    buttonRow->addWidget(cancelBtn);
    layout->addLayout(buttonRow, 3, 0, 1, 3);

    connect(browseBtn,  &QPushButton::clicked, this, &KIRIImportDialog::browseFile);
    connect(acceptBtn,  &QPushButton::clicked, this, &KIRIImportDialog::checkAccept);
    connect(cancelBtn,  &QPushButton::clicked, this, &QDialog::reject);
}

KIRIImportDialog::~KIRIImportDialog() = default;

QString KIRIImportDialog::selectedFile() const  { return filePathEdit->text(); }
double  KIRIImportDialog::scaleFactor() const   { return scaleSpinBox->value(); }
bool    KIRIImportDialog::generateBoundary() const { return boundaryCheckBox->isChecked(); }

void KIRIImportDialog::browseFile()
{
    QString path = QFileDialog::getOpenFileName(
        this, tr("Select KIRI Engine Export"), QString(),
        tr("3D Mesh/Point Cloud (*.obj *.ply);;All Files (*)"));
    if (!path.isEmpty())
        filePathEdit->setText(path);
}

void KIRIImportDialog::checkAccept()
{
    if (filePathEdit->text().trimmed().isEmpty()) {
        QMessageBox::warning(this, tr("KIRI Import"), tr("Please select a scan file."));
        return;
    }
    accept();
}
