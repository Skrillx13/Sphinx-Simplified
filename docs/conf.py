# -- Libary Import --
from datetime import datetime

# -- Project Information --
project = 'Sphinx Simplified'
copyright = f"{datetime.now().year}, A Srillx Project"
author = 'Skrillx'
release = '1.0'

# -- General Configuration --
extensions = [
    'myst_parser',
    'sphinx_design',
    ]
myst_enable_extensions = ["colon_fence"]
templates_path = ['templates']
html_static_path = ['assets']
exclude_patterns = ['build']
html_show_sphinx = False

# -- Theming --
html_theme = 'sphinx13-theme'
html_theme_path = ['..']
html_css_files = [
    'sphinx13-theme.css',
]