{# prevent the template from being escaped by cookiecutter #} {% raw %}
{% if style = 'tab' %}
.. grid:: 2

   .. grid-item-card::  reStructuredText

      {% for line in content %}{{ line }}
      {% endfor %}

   .. grid-item-card:: Result

      {% for line in content %}{{ line }}
      {% endfor %}
{% else %}
.. tab-set::

   .. tab-item:: Result

      {% for line in content %}{{ line }}
      {% endfor %}

   .. tab-item:: reStructuredText

      .. code:: rst
       
         {% for line in content %}{{ line }}
         {% endfor %}
{% endif %}
{% endraw %}
