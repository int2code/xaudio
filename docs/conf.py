# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# pylint: skip-file
from datetime import date

from pkg_resources import get_distribution

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "xaudio"
copyright = f"{date.today().year}, int2code"
author = "int2code"
version = release = get_distribution("xaudio").version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxcontrib.programoutput",
    "myst_parser",
]
autosummary_generate = True

# uncomment when _templates won't be empty
# templates_path = ['._templates']
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "README.md",  # this is readme describing how to generate docs
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# uncomment when static content is added
# html_static_path = ['_static']

# suppress warning from release notes and readme markdown files
suppress_warnings = ["myst.header"]
