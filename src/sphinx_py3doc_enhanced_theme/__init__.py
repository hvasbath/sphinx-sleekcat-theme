import os

__version__ = "2.1.0"


def get_html_theme_path():
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
