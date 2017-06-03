import os
from recommonmark.parser import CommonMarkParser

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

todo_include_todos = True

master_doc = 'index'

project = u'Hardops'
copyright = u'2015, Hops'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = ['includes/*']

pygments_style = 'sphinx'

htmlhelp_basename = 'AnimationNodesdoc'

latex_elements = {}
latex_documents = [
  ('index', 'AnimationNodes.tex', u'Hardops Documentation',
   u'Hops', 'manual'),
]

man_pages = [
    ('index', 'animationnodes', u'Hardops Documentation',
     [u'Hops'], 1)
]
texinfo_documents = [
  ('index', 'AnimationNodes', u'Hardops Documentation',
   u'Hops', 'AnimationNodes', 'A new way to work with data in Blender.',
   'Miscellaneous'),
]

epub_title = u'Hardops'
epub_author = u'Hops'
epub_publisher = u'Hops'
epub_copyright = u'2017, Hops'
epub_exclude_files = ['search.html']
