.. This file is generated from {{ cookiecutter.github_owner }}/cookiecutter.
   You need to consider modifying the TEMPLATE or modifying THIS FILE.

{% for _ in cookiecutter.full_name %}={% endfor %}
{{ cookiecutter.full_name }}
{% for _ in cookiecutter.full_name %}={% endfor %}

.. |docs| image:: https://img.shields.io/github/deployments/{{ cookiecutter.github_owner }}/{{ cookiecutter.name }}/github-pages?label=docs
   :target: https://sphinx.silverrainz.me/{{ cookiecutter.name }}
   :alt: Documentation Status
.. |license| image:: https://img.shields.io/github/license/{{ cookiecutter.github_owner }}/{{ cookiecutter.name }}
   :target: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}/blob/master/LICENSE
   :alt: Open Source License
.. |pypi| image:: https://img.shields.io/pypi/v/{{ cookiecutter.pypi_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.pypi_name }}
   :alt: PyPI Package
.. |download| image:: https://img.shields.io/pypi/dm/{{ cookiecutter.pypi_name }}
   :target: https://pypi.python.org/pypi/{{ cookiecutter.pypi_name }}
   :alt: PyPI Package Downloads
.. |github| image:: https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white/
   :target: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.name }}
   :alt: GitHub Repository

|docs| |license| |pypi| |download| |github|

Introduction
============

.. INTRODUCTION START

.. INTRODUCTION END

Getting Started
===============
{% if cookiecutter.is_sphinx_extension %}
.. note::

   We assume you already have a Sphinx documentation,
   if not, see `Getting Started with Sphinx`_.

{% endif -%}
{%- if cookiecutter.is_sphinx_extension %}
First, downloading extension from PyPI:

.. code-block:: console

   $ pip install {{ cookiecutter.pypi_name }}

{% endif -%}
{%- if cookiecutter.is_sphinx_extension %}
Then, add the extension name to ``extensions`` configuration item in your
:parsed_literal:`conf.py_`:

.. code-block:: python

   extensions = [
             # …
             '{{ cookiecutter.namespace }}.{{ cookiecutter.name }}',
             # …
             ]

.. _Getting Started with Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _conf.py: https://www.sphinx-doc.org/en/master/usage/configuration.html
{% endif %}
.. ADDITIONAL CONTENT START

.. ADDITIONAL CONTENT END

Contents
========

.. toctree::
   :caption: Contents

   changelog

The Sphinx Notes Project
========================

The project is developed by `{{ cookiecutter.author }}`__,
as part of **The Sphinx Notes Project**.

.. toctree::
   :caption: The Sphinx Notes Project

   Home <https://sphinx.silverrainz.me/>
   Blog <https://silverrainz.me/blog/category/sphinx.html>
   PyPI <https://pypi.org/search/?q={{ cookiecutter.namespace }}>

__ https://github.com/SilverRainZ
