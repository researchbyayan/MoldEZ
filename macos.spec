# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

project_dir = Path.cwd()
icon_icns = project_dir / "icon.icns"

a = Analysis(
    ['mkOS.py'],
    pathex=[str(project_dir)],
    binaries=[],
    datas=[
        ('banner.png', '.'),
        ('banner-dark.png', '.'),
        ('icon.icns', '.'),
    ],
    hiddenimports=[
        'roboflow',
        'roboflow.util',
        'roboflow.models',
        'matplotlib.backends.backend_tkagg',
        'reportlab',
        'cv2',
        'pillow_heif',
        'PIL.ImageTk',
        'tkinter',
        'PIL',
        'scipy',
        'scipy.ndimage',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MoldEZ',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(icon_icns) if icon_icns.exists() else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='MoldEZ',
)

app = BUNDLE(
    coll,
    name='MoldEZ.app',
    icon=str(icon_icns) if icon_icns.exists() else None,
    bundle_identifier='com.researchbyayan.moldez',
)
