extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['ytemplates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Code Autocomplete'
copyright = u'2015, Jacques Lucke'

version = '2.0.0'
release = '2.0.0'

exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['ystatic']

htmlhelp_basename = 'CodeAutocompleteManual'


latex_elements = {}
latex_documents = [
  ('index', 'CodeAutocomplete.tex', u'Code Autocomplete Manual',
   u'Jacques Lucke', 'manual'),
]

man_pages = [
    ('index', 'codeautocomplete', u'Code Autocomplete Manual',
     [u'Jacques Lucke'], 1)
]
texinfo_documents = [
  ('index', 'CodeAutocomplete', u'Code Autocomplete Manual',
   u'Jacques Lucke', 'CodeAutocomplete', 'Unleash the power of scripting in Blender',
   'Miscellaneous'),
]

epub_title = u'Code Autocomplete'
epub_author = u'Jacques Lucke'
epub_publisher = u'Jacques Lucke'
epub_copyright = u'2015, Jacques Lucke'
epub_exclude_files = ['search.html']
