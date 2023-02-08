#!/bin/bash

COOKIECUTTER=cookiecutter

repo=$(basename --suffix .git `git config --get remote.origin.url`)
root=$(git rev-parse --show-toplevel)

if [[ "$(basename $root)" != "$repo" ]]; then
    echo repository root directory must be consistent with the repository name:
    echo
    echo \t"$(basename $root)" != "$repo"
    exit 1
fi

# Generate project.
$COOKIECUTTER \
    --no-input \
    --overwrite-if-exists \
    --replay-file "$root/.{{cookiecutter.github_owner}}/template/cookiecutter_replay.json" \
    --output-dir "$(dirname $root)" \
    gh:{{cookiecutter.github_owner}}/template
