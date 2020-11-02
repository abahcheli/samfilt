from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

long_description = README

# automatically captured required modules for install_requires in requirements.txt
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup(
    name="samfilt", # Replace with your own username
    version="0.0.1",
    author="Alec Bahcheli",
    author_email="abahchel@uwo.ca",
    description="Sam file filtering script.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abahcheli/samfilt",
    packages=find_packages(),
    install_requires = install_requires,
    python_requires='>=3.0',
    scripts=['samfilt/samfilt'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Academic Free License (AFL)",
        "Operating System :: OS Independent",
    ]
)