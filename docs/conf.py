# Configuration file for Sphinx documentation

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = "Mushroom"
author = "suco2007"
release = "0.22.0"

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Paths for templates and static files
templates_path = ["_templates"]
html_static_path = ["_static"]

# Theme configuration
html_theme = "sphinx_rtd_theme"

# Master document (entry point)
master_doc = "index"

# Source file suffix
source_suffix = ".rst"

# Exclude patterns (files/folders to ignore)
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

copyright = "suco2007"

# Options for HTML output
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
}

# Autodoc settings
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True