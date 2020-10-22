---
layout: tags_header
title: Projects Categories
permalink: /tags/
---

<div>

{% comment %}
=======================
The following part extracts all the tags from your posts and sort tags, so that you do not need to manually collect your tags to a place.
=======================
{% endcomment %}
{% assign rawtags = "" %}
{% for post in site.work %}
	{% assign ttags = post.tags | join:'|' | append:'|' %}
	{% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% comment %}
=======================
The following part removes dulpicated tags and invalid tags like blank tag.
=======================
{% endcomment %}
{% assign tags = "" %}
{% for tag in rawtags %}
	{% if tag != "" %}
		{% if tags == "" %}
			{% assign tags = tag | split:'|' %}
		{% endif %}
		{% unless tags contains tag %}
			{% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
		{% endunless %}
	{% endif %}
{% endfor %}

{% comment %}
=======================
The purpose of this snippet is to list all your posts posted with a certain tag.
=======================
{% endcomment %}
{% for tag in tags %}
	<div class="archive-group">
	{% capture category_name %}{{ tag }}{% endcapture %}
	<div id="#{{ category_name | slugize }}"></div>
	<p></p>
	<h3 class="category-head">{{ category_name }}</h3>
	<a name="{{ category_name | slugize }}"></a>
	 {% for post in site.work %}
		 {% if post.tags contains tag %}
		 <article class="archive-item">
		 <h4>
		 <a href="{{ site.baseurl }}{{ post.url }}">
		 {{ post.title }}
		 </a>
		 </h4>
		 </article>
		 {% endif %}
	 {% endfor %}
	 </div>
{% endfor %}

</div>
