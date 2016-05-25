from setuptools import setup

setup(
    name='SNoBoL',
    version='0.2.1',
    description='Supernova Bolometric Lightcurves',
    author='Jeremy A. Lusk',
    author_email='jeremy.lusk@gmail.com',
    url='https://github.com/JALusk/SNoBoL',
    packages=['snobol'],
    package_data={'snobol' : ['data/sn_data.h5']},
    license='MIT License',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Astronomy",
        ],
    install_requires=[
        "astropy",
        "scipy>=0.14",
        "numpy",
        "specutils"
    ],
    )   
