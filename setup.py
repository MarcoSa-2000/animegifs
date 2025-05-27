from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

LONG_DESCRIPTION = long_description
VERSION = '1.2.1'

setup(
    name='animegifs',
    package_dir={"anime_gifs": "animegifs"},
    packages=["animegifs", "animegifs.distutils"],
    version=VERSION,
    description='Get random anime gifs by category.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Marco-Sa2000',
    author_email='grest0grest@gmail.com',
    license='MIT',
    url="https://github.com/MarcoSa-2000/animegifs",
    install_requires=[
       'requests>=2.32.2',
       'mal-api==0.5.3'
    ],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"],
    keywords=['anime', 'gif', 'python', 'anime-gifs', 'discord'],
)
