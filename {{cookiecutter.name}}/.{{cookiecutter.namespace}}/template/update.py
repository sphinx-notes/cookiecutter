#!/usr/bin/env python3

from cookiecutter.main import cookiecutter

# Create project from the cookiecutter-pypackage.git repo template
cookiecutter('gh:{{ cookiecutter.github_owner }}/template')
