# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/lincolnnguyen/workplace/FlaskPywebviewExample/FlaskPywebviewExampleApi/api/run.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/lincolnnguyen/workplace/FlaskPywebviewExample/FlaskPywebviewExampleApi/static', 'api/static')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,`
    [],
    name='Flask Pywebview Example',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='Flask Pywebview Example.app',
    icon='dist/Icon.icns',
    bundle_identifier='com.rinkaaan.FlaskPywebviewExample',
)