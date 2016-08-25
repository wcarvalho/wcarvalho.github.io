---
title: Poetry
layout: page
---

{% for node in site.posts %}
{% if node.title != null %}
{% if node.category == "poem" %}
  1. [{{ node.title }}]({{ node.url }}) <small>{{ node.date | date: '%B %d, %Y' }}</small>
  <br><em>{{ node.tags | join: ' ' }}</em>
{% endif %}
{% endif %}
{% endfor %}