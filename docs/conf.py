import os

project = "Magician ROS2 Messages"
copyright = "The Magician Consortium"
author = "The Magician Consortium"
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

index_var = os.environ.get("INDEX")
if index_var:
    master_doc = index_var
else:
    master_doc = "index"
