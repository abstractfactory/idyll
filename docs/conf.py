# -*- coding: utf-8 -*-

import sys
import os
import sphinx

src_path = os.path.abspath('..')
if not src_path in sys.path:
    sys.path.insert(0, src_path)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

if sphinx.version_info >= (1, 3):
    extensions.append('sphinx.ext.napoleon')
else:
    extensions.append('sphinxcontrib.napoleon')

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Idyll'
copyright = u'2014, Marcus Ottosson'
version = '0.1.0'
release = version

exclude_patterns = []
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

if os.environ.get('READTHEDOCS', None) != 'True':
    try:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    except ImportError:
        pass

html_static_path = ['_static']
htmlhelp_basename = 'Pipidoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

latex_documents = [
  ('index', 'Idyll.tex', u'Idyll Documentation',
   u'Marcus Ottosson', 'manual'),
]

man_pages = [
    ('index', 'Idyll', u'Idyll Documentation',
     [u'Marcus Ottosson'], 1)
]

texinfo_documents = [
  ('index', 'Idyll', u'Idyll Documentation',
   u'Marcus Ottosson', 'Idyll', 'Ideal pipeline setup for feature animation',
   'Miscellaneous'),
]