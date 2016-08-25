---
layout: page
title: Blog
---

This blog serves two purposes:

1. As I continue to explore how the brain functions, it gives me a medium to share what I discover, communicate my progress, and teach others what I learn.
2. It provides a platform to share my experiences with a variety of topics. E.g. time and task management, navigating the educational landscape, useful software, etc.

For my posts, I upload and reference material I think is useful (articles, code snippets, etc). <a href="{{ site.baseurl }}/reference_material">This</a> is an aggregate of all of these items.
<br>

## Posts

<ol>
{% for post in site.posts %}
<li>
  <a href="{{ post.url }}">
    {{ post.title }}
  </a>
  {% if post.categories.size > 0 %}
   | <cite> {{ post.categories | join: ' ' }} </cite>
  {% endif %}
  {{ post.date | date: '%B %d, %Y' }}
  {% if post.tags.size > 0 %}
  <br>
  <em>
    tags: {{ post.tags | join: ' ' }}
  </em>
  {% endif %}
  
</li>
{% endfor %}
</ol>
