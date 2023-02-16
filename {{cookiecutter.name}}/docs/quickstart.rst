.. This file is generated from {{ cookiecutter.github_owner }}/template. DO NOT EDIT.

===============
Getting Started
===============

.. note::

   We assume you already have a Sphinx documentation,
   if not, see `Getting Started with Sphinx`_.

First, downloading extension from PyPI (see :doc:`install` for more details):

.. code-block:: console

   $ pip install {{ cookiecutter.pypi_name }}

Then, add the extension name to ``extensions`` configuration item in your conf.py_:

.. code-block:: python

   extensions = [
             # …
             '{{ cookiecutter.namespace }}.{{ cookiecutter.name }}',
             # …
             ]

.. _Getting Started with Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _conf.py: https://www.sphinx-doc.org/en/master/usage/configuration.html

.. include:: usage_for_quickstart.rst
