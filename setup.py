from setuptools import setup, find_packages

setup(
    name='tarsier',
    version='0.0.0',
    packages=find_packages(exclude=['tests*']),
    license='NDA',
    description='describe() on steroids - DASKified',
    long_description=open('README.md').read(),
    url='https://github.com/neuronist/tarsier',
    package_dir={
        'tarsier': 'tarsier/'
    },
    author='neuronist',
    author_email='deepneuronist@gmail.com',
    tests_require=['pytest'],
    install_requires=[
        'dask[complete]',
        'pandas',
        'numpy',
        'scipy',  # dask array needs this
    ],
)