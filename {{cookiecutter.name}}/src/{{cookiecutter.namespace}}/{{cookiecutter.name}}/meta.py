# This file is generated from {{ cookiecutter.github_owner }}/cookiecutter.
# DO NOT EDIT!!!

################################################################################
# Project meta infos.
################################################################################

from __future__ import annotations
from importlib import metadata

__project__ = "{{ cookiecutter.full_name }}"
__author__ = "{{ cookiecutter.author }}"
__desc__ = "{{ cookiecutter.description }}"

try:
    __version__ = metadata.version('{{ cookiecutter.pypi_name }}')
except metadata.PackageNotFoundError:
    __version__ = 'unknown'

#{% if cookiecutter.is_sphinx_extension %}
################################################################################
# Sphinx extension utils.
################################################################################

def pre_setup(app):
    app.require_sphinx('{{ cookiecutter.sphinx_version }}')

def post_setup(app):
    return {
        'version': __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
#{% endif %}
