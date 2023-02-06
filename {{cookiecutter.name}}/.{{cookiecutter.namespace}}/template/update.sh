#!/bin/bash

repo=$(basename --suffix .git `git config --get remote.origin.url`)
root=$(git rev-parse --show-toplevel)

if [[ "$PWD" != "$root" ]]; then
    echo PWD must be at the root of the repository
    exit 1
fi

git submodule update --init

# Generate cookiecutter.json for current project.
cd "$root/.{{ cookiecutter.namespace }}/template"
./gen_cookiecutter_json.py "$repo"

# Generate project.
cd "$root/.."
cookiecutter ./template --no-input --overwrite-if-exists
