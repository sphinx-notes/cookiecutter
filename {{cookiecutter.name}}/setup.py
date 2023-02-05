# This file is generated from {{ cookiecutter.github_owner }}/template. DO NOT EDIT.

"""
Setup file for {{ cookiecutter.full_name }}.
Use pyproject.toml to configure your project.
"""
from setuptools import setup

if __name__ == "__main__":
    try:
        setup(use_scm_version={"version_scheme": "no-guess-dev"})
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
