---
layout: home
---

{% for post in site.posts %}
<!-- ## [{{ post.title }}]({{ post.url }}) -->
<article>
  <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>

  <p>
    {% assign sentences = post.content | strip_html | newline_to_space | split: '.' %}
    {% for sentence in sentences limit:2 %}
      {{ sentence | strip }}.
    {% endfor %}
    <a href="{{ post.url }}">Read more &raquo;</a>
  </p>

</article>

{% endfor %}
