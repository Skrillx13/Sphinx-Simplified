# -- Library Import --
from datetime import datetime

# -- Project Information --
project = 'Sphinx Simplified'
copyright = f"{datetime.now().year}, A Skrillx Project"
author = 'Skrillx13'
release = '1.0'

# -- General Configuration --
extensions = [
    'myst_parser',
    'sphinx_design',
]
myst_enable_extensions = ["colon_fence"]
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build']

# -- Theming --
html_theme = 'sphinx13-theme'
html_theme_path = ['..']
html_css_files = [
    'sphinx13-theme.css',
]