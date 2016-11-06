import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo'
]

todo_include_todos = True

templates_path = ['ytemplates']
source_suffix = '.rst'
master_doc = 'index.rst'

project = u'Hops'
copyright = u'2016, Hops'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = ['includes/*']

pygments_style = 'sphinx'

htmlhelp_basename = 'Hops'

latex_elements = {}
latex_documents = [
  ('index', 'Hops.tex', u'Hops Documentation',
   u'Hops', 'manual'),
]

man_pages = [
    ('index', 'Hops', u'Hops Documentation',
     [u'Hops'], 1)
]
texinfo_documents = [
  ('index', 'Hops', u'Hops Documentation',
   u'Hops', 'Hops', 'Hops',
   'Miscellaneous'),
]

epub_title = u'Hops'
epub_author = u'Hops'
epub_publisher = u'Hops'
epub_copyright = u'2016, Hops'
epub_exclude_files = ['search.html']

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']