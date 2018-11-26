#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

long_description = open('README.md').read()
version = '1.0.0'

setup(
	name='Tome',    # This is the name of your PyPI-package.
	description='Temperature optima for microorgianisms and enzymes',#package description
    long_description=long_description,
    version=version,                          # MAJOR.MINOR.PATCH
	author='Gang Li',
	author_email='gangl@chalmers.se',
	url='https://github.com/EngqvistLab/Tome',
    packages=find_packages(exclude=['test*']), #find folders containing scripts, exclude irrelevant ones
	# package_dir={'':'tome'},
    install_requires=['pandas','Biopython','numpy','collections','sklearn'],
    include_package_data=True,
    package_data={'tome':['data/train.csv',
						  'model/OGT_svr.f',
						  'model/OGT_svr.pkl',
						  'external_data/2_unid_growth_temp_mapping.tsv',
						  'external_data/all_enzyme_sequences.fasta']},
	license='Apache License 2.0',
	classifiers=[
	# How mature is this project? Common values are
	#   3 - Alpha
	#   4 - Beta
	#   5 - Production/Stable
	'Development Status :: 3 - Alpha',

	# Indicate who your project is intended for
	'Intended Audience :: Science/Research',
	'Topic :: Scientific/Engineering',

	# Pick your license as you wish (should match "license" above)
	'License :: OSI Approved :: Apache Software License',

	# Specify the Python versions you support here. In particular, ensure
	# that you indicate whether you support Python 2, Python 3 or both.
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.2',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6'],
    python_requires='>=2', #python version
    keywords='tome',
	entry_points={
        'console_scripts': [
            'tome = tome:main'
        ]
    }
)