---
title: Poetry
layout: page
---

<section class="bg-white" id="portfolio">
<div class="container">
<div class="row">

{% for node in site.posts %}
{% if node.title != null %}
{% if node.category == "poem" %}


<div class="col-md-4 col-sm-6 portfolio-item">
<a class="portfolio-link" data-toggle="modal" href="{{ node.url }}">
<div class="portfolio-hover">
<div class="portfolio-hover-content">
  <i class="fa fa-plus fa-3x">{{ node.caption }}</i>
</div>
</div>
<img class="img-fluid" src="{{ node.img }}" alt="">
</a>
<div class="portfolio-caption">
  <h4>{{ node.title }}</h4><small>{{ node.date | date: '%B %d, %Y' }}</small>
  <p class="text-muted">{{ node.tags | join: ', ' }}</p>
</div>
</div>

{% endif %}
{% endif %}
{% endfor %}


</div>
</div>
</section>