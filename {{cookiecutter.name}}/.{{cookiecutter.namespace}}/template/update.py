#!/usr/bin/env python3

from os import path
import subprocess
from cookiecutter.main import cookiecutter
from github import Github

def run_shell(*args: str) -> str:
    return subprocess.run(args, capture_output=True, text=True).stdout

# Fetch meta information.
root = run_shell('git', 'rev-parse', '--show-toplevel')
repo = path.basename(root)
version = run_shell('git', 'describe', '--tags')
desc = Github().get_user('{{ cookiecutter.github_owner }}').get_repo('{{ cookiecutter.github_repo }}')

# Create project from the remote repository template.
# .. seealso::
#    - https://cookiecutter.readthedocs.io/en/1.7.2/cookiecutter.html#module-cookiecutter.main
#    - https://cookiecutter.readthedocs.io/en/1.7.2/advanced/injecting_context.html
cookiecutter('gh:{{ cookiecutter.github_owner }}/template',
             checkout="submodule",
             no_input=True,
             overwrite_if_exists=True,
             output_dir=root,
             extra_context={
                 'name': repo,
                 'version': version,
             })
