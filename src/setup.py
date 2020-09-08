import io
from setuptools import setup, find_packages

from ml_research_toolkit import __version__

def read(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


readme = read('README.rst')
requirements = read('requirements.txt')


setup(
    # metadata
    name='ml-research-toolkit',
    version=__version__,
    license='MIT',
    author='Andrey Grabovoy',
    author_email="grabovoy.av@phystech.edu",
    description='toolkits for machine learning, python package',
    long_description=readme,
    url='https://github.com/andriygav/MLResearchToolkit',

    # options
    packages=find_packages(),
    python_requires='==3.*',
    install_requires=requirements,
)