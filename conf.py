import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Система управления задачами'
copyright = '2024, Vadim'
author = 'Vadim'

# Конфигурация расширений Sphinx
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary'
]

# Настройки путей
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']

# Настройки HTML
html_theme = 'sphinx_rtd_theme'
html_static_path = []

# Языковые настройки
language = 'ru'
locale_dirs = ['locale/']
gettext_compact = False