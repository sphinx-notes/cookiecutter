{# prevent the template from being escaped by cookiecutter #} {% raw %}
:ref:`📅{{ date }} <any-version.date>` | :tag:`{{ title }}`

{% for line in content %}
{{ line }}
{% endfor %}
{% endraw %}
