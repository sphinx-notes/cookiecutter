#!/usr/bin/env python3

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

    # Documentation meta information.
    # additional_docs: dict[str,str] # FIXME: ust list[str]: IndexError: list index out of range

    # Other projects.
    others: dict[str,str] # name -> description

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
        # self.additional_docs = {}
        self.others = {x: 'DESCRIPTION' for x in ALL_PROJECTS if x != name}

        # Fill self-reference fields.
        self.full_name = f'{self.namespace}-{self.name}'
        self.github_repo = self.name
        self.pypi_name = self.full_name

        # Fetch dynamic fields from Github.
        repo = Github().get_user(self.github_owner).get_repo(self.github_repo)
        self.description = repo.description

    def to_json(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, indent=4)


p = Project('strike')

with open('./cookiecutter.json', 'w') as f:
    f.write(p.to_json())
