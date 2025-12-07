# Configuration file for the Sphinx documentation builder.

import os
import sys

# Project information
project = 'XAI Mini-Projet : Attention is Not Explanation'
copyright = '2025, Étudiants'
author = '[Nom Étudiant 1] & [Nom Étudiant 2]'
release = '1.0'

# Add source directory to path
sys.path.insert(0, os.path.abspath('.'))

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.napoleon',
]

# Theme
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#3498db',
}

# HTML output options
html_static_path = ['_static']
html_logo = None
html_favicon = None

# LaTeX output options
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
}

# Source suffix
source_suffix = '.rst'

# Master doc
master_doc = 'index'
