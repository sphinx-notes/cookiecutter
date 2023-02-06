#!/usr/bin/env python3

import sys
import json

from github import Github

ALL_PROJECTS = [
    'any',
    'extweb',
    'isso',
    'lilypond',
    'strike',
    'mock',
    'pages',
    'recentupdate',
    'snippet',
    'strike',
]

class Project:
    """ This object will be converted to cookiecutter.json prompts file. """

    #: Project meta information.
    namespace: str
    name: str
    version: str
    full_name: str
    description: str

    #: Author meta information.
    author: str

    # Github meta information.
    github_owner: str
    github_repo: str

    # Pypi meta information.
    pypi_owner: str
    pypi_name: str

    # Other projects.
    others: list[list[str]]

    # Documentation meta information.
    additional_docs: list[list[str]]

    def __init__(self, name: str):
        if name not in ALL_PROJECTS:
            raise Exception(f'Project {name} not in {ALL_PROJECTS}')
        else:
            self.name = name

        # Fill static fields.
        self.namespace = 'sphinxnotes'
        self.version = '0.1.0'
        self.author= 'Shengyu Zhang'
        self.github_owner = 'sphinx-notes'
        self.pypi_owner = 'SilverRainZ'
        # NOTE: We use list[list[str]] here because in cookiecutter.json,
        # the outer array is used as choice variables.
        # check out https://cookiecutter.readthedocs.io/en/latest/advanced/choice_variables.html
        self.others = [[x for x in ALL_PROJECTS if x != name]]
        self.additional_docs = [[]]

        # Fill self-reference fields.
        self.full_name = f'{self.namespace}-{self.name}'
        self.github_repo = self.name
        self.pypi_name = self.full_name

        # Fetch dynamic fields from Github.
        repo = Github().get_user(self.github_owner).get_repo(self.github_repo)
        self.description = repo.description

    def to_json(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, indent=4)


p = Project(sys.argv[1])

with open('./cookiecutter.json', 'w') as f:
    f.write(p.to_json())
