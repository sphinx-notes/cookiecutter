============
Installation
============

.. highlight:: console

.. note:: We assume you already have Python 3 environment and have pip_ in your ``PATH``.

The easiest way of installation is downloading extension from PyPI (Python Package Index)::

   $ pip install {{ cookiecutter.pypi_name }}

.. _pip: https://pip.pypa.io/en/stable/

Install from Source
===================

If the version you need has not been published to PypI, you can install from source.

pip can also install from git repository::

    $ pip install git+https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}.git@master

Or you can clone repository to local::

    $ git clone https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}.git

Then execute the following commands to build and install the extension::

    $ make install
