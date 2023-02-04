{% for _ in cookiecutter.full_name %}={% endfor %}
{{ cookiecutter.full_name }}
{% for _ in cookiecutter.full_name %}={% endfor %}

.. image:: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_owner }}/{{ cookiecutter.name }}/pages.yml
   :target: https://sphinx.silverrainz.me/{{ cookiecutter.name }}
   :alt: Documentation Status

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_owner }}/{{ cookiecutter.name }}
   :target: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}/LICENSE
   :alt: Open Source License

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.pypi_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.pypi_name }}
   :alt: PyPI Package

.. image:: https://img.shields.io/pypi/dw/{{ cookiecutter.pypi_name }}
   :target: https://pypi.python.org/pypi/{{ cookiecutter.pypi_name }}
   :alt: PyPI Package Downloads

* Documentation: https://sphinx.silverrainz.me/{{ cookiecutter.name }}
* Source: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}
* Changelog: https://sphinx.silverrainz.me/{{ cookiecutter.name }}/changelog.html
* Tracker: https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}/issues
* Download: https://pypi.org/project/{{ cookiecutter.pypi_name }}/#files
