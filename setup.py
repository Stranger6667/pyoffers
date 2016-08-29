# coding: utf-8
from setuptools import setup

import pyoffers


setup(
    name='pyoffers',
    url='https://github.com/Stranger6667/pyoffers',
    version=pyoffers.__version__,
    packages=['pyoffers', 'pyoffers.models'],
    license='MIT',
    author='Dmitry Dygalo',
    author_email='dadygalo@gmail.com',
    maintainer='Dmitry Dygalo',
    maintainer_email='dadygalo@gmail.com',
    keywords=['hasoffers', 'api', 'client'],
    description='Python client library for HasOffers API',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    include_package_data=True,
    install_requires=['requests'],
)
