#!/usr/bin/env python
"""Pronounced SY PIE, like "sirius python", sipie is a library and a online player for Sirius online Internet streaming. It requires a login to Sirius's streaming, and both guest and subscriber logins are supported. It provides the a back end and a usable cli and gui example"""


classifiers = """\
Development Status :: 4 - Beta
Environment :: Console
Environment :: X11 Applications :: GTK
Intended Audience :: End Users/Desktop
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Programming Language :: Python
Topic :: Multimedia :: Sound/Audio :: Players
Topic :: Software Development :: Libraries :: Python Modules
"""
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

doclines = __doc__.split("\n")

setup(
    name='Sipie',
    version='0.1196144357',
    description='Library and Player for Sirius Online Streaming',
    author='Eli Criffield',
    author_email='python@zendo.net',
    url='http://sipie.sourceforge.net/',
    license='http://www.gnu.org/licenses/gpl.txt',
    platforms=['any'],
    classifiers = filter(None, classifiers.split("\n")),
    packages= find_packages(),
    zip_safe = True,
    scripts=[ 'sipie.py' ],
    include_package_data = True,
    install_requires = { 'BeautifulSoup':  ["BeautifulSoup>=3.0"] },
    extras_require = { 'PyGTK': ["PyGTK>=2.0"], 'wxPython': ['wxPython>=2.6'] },
    entry_points = {
        'console_scripts': 
            [ 'cliSipie = Sipie:cliPlayer' ],
        'gui_scripts': 
            #[ 'gtkSipie = Sipie:gtkPlayer [PyGTK]' ]
            [ 'gtkSipie = Sipie:gtkPlayer',
               'wxSipie = Sipie:wxPlayer' ]
      }
)
