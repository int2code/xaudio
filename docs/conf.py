# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# pylint: skip-file
from pathlib import Path

ROOT_DIR = Path('..').resolve()
with open(ROOT_DIR / "version.txt") as fh:
    VERSION = fh.read()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'int2code-xaudio'
copyright = '2025, int2code'
author = 'int2code'

version = VERSION
release = VERSION

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinxcontrib.programoutput',
    'myst_parser'
]
autosummary_generate = True

# uncomment when _templates won't be empty
# templates_path = ['._templates']
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store', 
    'README.md'  # this is readme describing how to generate docs
    ]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# uncomment when static content is added
# html_static_path = ['_static']

# suppress warning from release notes and readme markdown files
suppress_warnings = ["myst.header"]
