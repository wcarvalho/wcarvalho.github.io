---
layout: page
title: Blog
---

This blog serves two purposes:
1. As I continue to explore how the brain functions, it gives me a medium to share what I discover, communicate my progress, and teach others what I learn.
2. It provides a platform to share my experiences with a variety of topics. E.g. time and task management, navigating the educational landscape, useful software, etc.

For my posts, I upload and reference material I think is useful (articles, code snippets, etc). <a href="{{ site.baseurl }}/reference_material.html">This</a> is an aggregate of all of these items.
<br>
## Posts

{% for post in site.posts %}
  1. [{{ post.title }}]({{ post.url }}) {{ post.date | date: '%B %d, %Y' }}
{% endfor %}
  
<!-- <p class="message">
{{post.excerpt}}
</p> -->
