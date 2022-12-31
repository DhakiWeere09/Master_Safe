# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_data = [
		('D:\\Programming\\DK\'S\\Python\\Master_Safe\\Images\\*.png', '.')
		]

a = Analysis(['Master_Safe_GUI.py'],
             pathex=["D:\\Programming\\DK'S\\Python\\Master_Safe"],
             binaries=[],
             datas= added_data,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Master_Safe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
		  icon="icon.ico"
		  )
