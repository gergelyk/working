from setuptools import setup, find_packages

setup(
    name = 'working',
    version = '0.1.0',
    description = 'Makes spawning processes enjoyable.',
    author = 'Grzegorz Krason',
    author_email = 'grzegorz.krason@gmail.com',
    url = 'https://pypi.org/project/working/',
    license = 'MIT',
    packages = find_packages(),
    keywords = 'process multiprocessing spawn join'.split(),
    classifiers = [],
    install_requires = [],
)

