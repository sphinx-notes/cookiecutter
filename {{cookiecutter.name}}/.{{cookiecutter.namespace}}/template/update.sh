#!/bin/bash

COOKIECUTTER=cookiecutter

root=$(git rev-parse --show-toplevel)

# Generate project.
$COOKIECUTTER \
    --overwrite-if-exists \
    --output-dir "$(dirname $root)" \
    --replay-file "$root/.{{cookiecutter.namespace}}/template/cookiecutter_replay.json" \
    --checkout submodule \
    gh:{{cookiecutter.github_owner}}/template

# --no-input \
# --replay-file "$root/.{{cookiecutter.namespace}}/template/cookiecutter_replay.json" \
