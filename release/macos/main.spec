# -*- mode: python -*-

block_cipher = None
from kivy.tools.packaging.pyinstaller_hooks import get_deps_all, hookspath, runtime_hooks

a = Analysis(['/Users/chris/wgu/C964T/src/main.py'],
             pathex=['/Users/chris/wgu/C964T'],
             cipher=block_cipher,
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             **get_deps_all())

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='C964T',
          debug=False,
          strip=False,
          upx=True,
          console=False )

coll = COLLECT(exe, 
               Tree('/Users/chris/wgu/C964T/src'),
               Tree('/Users/chris/wgu/C964T/data'),
               Tree('/Users/chris/wgu/C964T/imgs'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='C964T')

app = BUNDLE(coll,
             name='C964.app',
             icon=None,
             bundle_identifier=None)
