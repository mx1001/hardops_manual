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
master_doc = 'index'

project = u'HardOps'
copyright = u'2016, masterxeon1001'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = ['includes/*']

pygments_style = 'sphinx'

htmlhelp_basename = 'HardOpsdoc'

latex_elements = {}
latex_documents = [
  ('index', 'HardOps.tex', u'HardOps Documentation',
   u'masterxeon1001', 'manual'),
]

man_pages = [
    ('index', 'HardOps', u'Modelling Toolkit',
     [u'masterxeon1001'], 1)
]
texinfo_documents = [
  ('index', 'HardOps', u'HardOps Manual',
   u'masterxeon1001', 'HardOps', 'Modelling toolkit.',
   'Miscellaneous'),
]

epub_title = u'Hard Ops'
epub_author = u'masterxeon1001'
epub_publisher = u'masterxeon1001'
epub_copyright = u'2016, masterxeon1001'
epub_exclude_files = ['search.html']
