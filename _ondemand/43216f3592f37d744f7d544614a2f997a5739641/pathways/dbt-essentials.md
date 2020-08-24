---
layout: overview
title: dbt essentials
---

# {{ page.title }} Pathway

<ol>

{% assign pathway = site.data.ondemand.pathways | where: "title", "dbt essentials" %}
{% for path in pathway %}
  {% for module in path.modules %}
    {% assign modslug = module.slug %}
    {% assign mod = site.data.ondemand.modules | where: "slug", modslug %}
    {% for md in mod %}
      <li> <a href="/ondemand/{{ site.onDemandHash }}/{{ module.slug }}/{{ md.pages[0].slug }}">{{ module.name }}</a></li>
    {% endfor %}
  {% endfor %}
{% endfor %}

</ol>
