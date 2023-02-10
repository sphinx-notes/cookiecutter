.. This file is generated from {{ cookiecutter.github_owner }}/template. DO NOT EDIT.

.. include:: ../README.rst

Introduction
============

.. include:: intro_for_index.rst

You can quickly learn how to use this extension from :doc:`quickstart`.

Contents
========

.. toctree::
   :caption: Contents

   quickstart
   install
   usage
   conf
   changelog
   {% for d in cookiecutter.additional_docs %}
   {{ d }}
   {%- endfor %}

The Sphinx Notes Project
========================

This project is a developed by `{{ cookiecutter.author }}`__,
as part of **The Sphinx Notes Project**.

.. toctree::
   :caption: The Sphinx Notes Project

   Home <https://sphinx.silverrainz.me/>
   Blog <https://silverrainz.me/blog/category/sphinx.html>
   PyPI <https://pypi.org/search/?q={{ cookiecutter.namespace }}>

__ https://github.com/SilverRainZ
