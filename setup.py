# -*- coding: utf-8 -*-
"""`swri_sphinx_theme` lives on `Github`_.

.. _github: https://www.github.com/HardRockMartian/swri_sphinx_theme

"""
from setuptools import setup
from swri_sphinx_theme import __version__


setup(
    name='swri_sphinx_theme',
    version=__version__,
    url='https://github.com/HardRockMartian/swri_sphinx_theme/',
    license='MIT',
    author='HardRockMartian',
    author_email='anon@anon.net',
    description='Fork of ReadTheDocs.org theme for Sphinx, 2013 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['swri_sphinx_theme'],
    package_data={'swri_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
