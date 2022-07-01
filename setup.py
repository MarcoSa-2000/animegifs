from setuptools import find_packages, setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

LONG_DESCRIPTION = long_description
VERSION = '0.2.3'

setup(
    name='animegifs',
    packages=find_packages(),
    version=VERSION,
    description='Get random anime gifs by category.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Marco-Sa2000',
    author_email='grest0grest@gmail.com',
    license='MIT',
    url="https://github.com/MarcoSa-2000/animegifs",
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"],
    keywords=['anime', 'gif', 'python', 'anime-gif'],
)
