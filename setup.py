from distutils.core import setup
import py2exe

setup(console=['rect.py'],
      options={
          'py2exe': {
              'packages': ['reportlab'],
              'bundle_files': 3
          }
      })