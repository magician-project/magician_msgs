project = "Magician ROS2 Messages"
copyright = "The Magician Consortium"
# author = ""
# release = ""

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinxcontrib.mermaid", 
    "myst_parser",
]

pygments_style = 'sphinx'

html_theme = 'furo'
autosummary_generate = True
myst_enable_extensions = ["deflist"]
