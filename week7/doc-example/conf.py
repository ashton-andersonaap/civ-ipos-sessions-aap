project = 'Test sphinx project'
author = 'Alice, Bob'
release = '0.1'

extensions = ['myst_nb', "sphinx.ext.autodoc"]

autodoc_packages = ['multiply.py']

exclude_patterns = ['_build']

html_theme = 'sphinx_rtd_theme'