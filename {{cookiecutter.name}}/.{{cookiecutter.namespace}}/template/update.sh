#!/bin/bash

cookiecutter=cookiecutter

repo=$(basename --suffix .git `git config --get remote.origin.url`)
root=$(git rev-parse --show-toplevel)

if [[ "$(basename $root)" != "$repo" ]]; then
    echo repository root directory must be consistent with the repository name:
    echo
    echo \t"$(basename $root)" != "$repo"
    exit 1
fi

if [[ "$PWD" != "$root" ]]; then
    echo PWD must be root directory of the repository:
    echo
    echo \t"$PWD" != "$root"
    exit 1
fi

# git submodule update --init

# Generate cookiecutter.json for current project.
"$root/.{{ cookiecutter.namespace }}/template/template/gen_cookiecutter_json.py" "$repo"

cd "$root/.."
# Generate project.
$cookiecutter ./template --no-input --overwrite-if-exists
