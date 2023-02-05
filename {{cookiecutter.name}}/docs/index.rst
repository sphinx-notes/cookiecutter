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

Other Projects
==============

There are other Sphinx extensions provided by the `Sphinx Notes Project`_ that you might be interested in:

.. toctree::
   :caption: Other projects:

   {% for p in cookiecutter.others %}
   {{ p }} <https://sphinx.silverrainz.me/{{ p }}>{% endfor %}

.. _Sphinx Notes Project: https://sphinx.silverrainz.me
