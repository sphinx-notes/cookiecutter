{# prevent the template from being escaped by cookiecutter #} {% raw %}
:Date: :ref:`📅{{ date }} <any-version.date>`
:Download: :tag:`{{ title }}`

{% for line in content %}
{{ line }}
{% endfor %}
{% endraw %}
