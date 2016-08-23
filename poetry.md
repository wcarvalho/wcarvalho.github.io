---
title: Poetry
layout: page
---

{% for node in site.pages %}
{% if node.title != null %}
{% if node.layout == "poem" %}
  1. [{{ node.title }}]({{ node.url }})
{% endif %}
{% endif %}
{% endfor %}