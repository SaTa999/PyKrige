#! /usr/bin/env python
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy


DESCRIPTION = 'pyKrig: Kriging & ANOVA implemted in python'
DISTNAME = 'pyKrig'
MAINTAINER = 'STakanashi'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/SaTa999/pyKrig'
VERSION = '0.1.0'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():
    install_requires = []
    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import scipy
    except ImportError:
        install_requires.append('scipy')
    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')
    return install_requires


try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False


if USE_CYTHON:
    ext_modules = [
    Extension("pyKrig.utilities.krig", sources=["pyKrig.utilities.krig.pyx"], extra_compile_args=['/O2']),
    Extension("pyKrig.utilities.lhs", sources=["pyKrig.utilities.lhs.pyx"], extra_compile_args=['/O2'])
    ]
    cmdclass = {'build_ext': build_ext}
else:
    ext_modules = [
    Extension("pyKrig.utilities.krig", sources=["pyKrig.utilities.krig.c"], extra_compile_args=['/O2']),
    Extension("pyKrig.utilities.lhs", sources=["pyKrig.utilities.lhs.c"], extra_compile_args=['/O2'])
    ]
    cmdclass = {}


if __name__ == "__main__":
    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          maintainer=MAINTAINER,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['pyKrig'],
          package_dir={'pyKrig.utilities'},
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 3.6',
              'License :: OSI Approved :: MIT License',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows'],
          cmdclass = cmdclass,
          ext_modules = ext_modules,
          include_dirs=[numpy.get_include()]
          )
