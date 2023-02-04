default: cookiecutter.json
	cookiecutter . --no-input --output-dir ./output --overwrite-if-exists

cookiecutter.json:
	./gen_cookitecutter_json.py
