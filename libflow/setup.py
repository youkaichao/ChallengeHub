from distutils.core import setup, Extension

module1 = Extension('libflow', sources=['main.c'])

setup(name='libflow',
      version='1.0',
      description='This is a network flow package',
      ext_modules=[module1])

# python setup.py build_ext --inplace
