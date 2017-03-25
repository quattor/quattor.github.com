##### Overview
  * [Getting Started](/documentation/getting-started.html)

{% comment %}
Documentation categories must match a Jekyll collection name.
If the collection name contains underscores, they are replaced by space in the documentation menu
{% endcomment %}
{% assign submenu_categories = "quattor, aquilon, development" | split: ", " %}
{% for topic in submenu_categories %}
  {% assign topic_words = topic | split: "_" %}
  {% capture topic_title %}{% for word in topic_words %}{{ word | capitalize }} {% endfor %}{% endcapture %}
##### {{ topic_title }}
  {% comment %}FIXME: When Jekyll uses Liquid v4, use %- for a more readable line without additional new lines{% endcomment %}
  {% for page in site[topic] %}
  {% capture menu_item %}{% if page.menu %}{{ page.menu }}{% else %}{{ page.title }}{% endif %}{% endcapture %}* [ {{ menu_item }} ]( {{ page.url }} ){% endfor %}
{% endfor %}

##### Other
  * [Other articles](/documentation/other.html)
