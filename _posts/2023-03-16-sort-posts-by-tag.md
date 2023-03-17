---
layout: post-narrow
title: How to show Jekyll posts from one category, sorted by tags
date: 2023-03-16 10:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Markup', 'Jekyll']
---

Here is my solution that allows your Jekyll page to show blog posts from one category, sorted by tags. 

<!--excerpt-->

Like this:

<img src="/images/tutorial_sort_tag/outcome.png"  width="60%" height="60%">

We'll use the `category`/`categories` and the `tags` variables in Jekyll posts' front matter. 

First, in your `year-month-date-post.md` in the `_posts` folder, put down both the post's category (which will be used to select whether this post shows up on a specific page at all), and its tags (which the page will use to sort where the post shows up on the page). For example, this post will only show up on a page that shows the category `'Casual posts'`, and it will show under the `'Food'` section: 

```
---
layout: post
categories: ['Casual posts']
tags: ['Food']
---

Example text

<!--excerpt-->

Example text Example text Example text Example text Example text Example text 
```

Insert `<!--excerpt-->` to separate the post excerpt from other texts. 

In the `page.md` where you want to show posts, specify the category and the tags of posts to show on this page. If your post satisfy more than one tag specified in `tags`, the post will show up more than once. For example, this page will only show posts with the category `'Casual posts'` and at least one of the following tags: `'Food'`, `'Travel'`, or `'My hobbies'`: 
```
---
layout: my-layout
title: Example sort by category page
permalink: /my-blog/
category: 'Casual posts'
tags: ['Food', 'Travel', 'My hobbies']
---
```

In your `my-layout.html` in the `_layouts` folder, use for loops to (1) make a list of tags to allow readers to easily navigate to each tag; and (2) show posts sorted by tags. 

{% raw %}
<pre><code>&lt;div class=&quot;home&quot;&gt;
{%- if page.title -%}
    &lt;h1 class=&quot;page-heading&quot;&gt;{{ page.title }}&lt;/h1&gt;
{%- endif -%}

&lt;!-- a list of tags to show up at the top of the page --&gt;
&lt;ul  style=&quot;list-style-type: none&quot;&gt;
    {% for i in page.tags %}
        &lt;li&gt;&lt;a href=&quot;#{{ i }}&quot;&gt;{{ i }}&lt;/a&gt;&lt;/li&gt;
    {% endfor %}
&lt;/ul&gt;

{{ content }}

&lt;!-- sort posts by tags --&gt;
{% for item in page.tags %}
    &lt;h2 style=&quot;margin: 1.5em 0 0 0;&quot;&gt;{{ item }}&lt;/h2&gt;&lt;a name=&quot;{{ item }}&quot;&gt;&lt;/a&gt;
    &lt;ul style=&quot;list-style-type: none&quot;&gt;
    {% for post in site.tags[item] %}
        &lt;li&gt;
        &lt;h3&gt;
            &lt;a class=&quot;post-link&quot; href=&quot;{{ post.url | relative_url }}&quot;&gt;
                {{ post.title | escape }}
            &lt;/a&gt;
        &lt;/h3&gt;
        &lt;span class=&quot;post-meta&quot;&gt;{{ post.date | date_to_long_string }}&lt;/span&gt;
        {{ post.excerpt }}
        {% if post.content contains site.excerpt_separator %}
            &lt;a href=&quot;{{ site.baseurl }}{{ post.url }}&quot;&gt;Read more&lt;/a&gt;
        {% endif %}
        &lt;/li&gt;
    {% endfor %}
    &lt;/ul&gt;
{% endfor %}

&lt;/div&gt;
</code></pre>
{% endraw %}

Finally, in your site's `_config.yml`, specify the excerpt separator:
```
excerpt_separator: "<!--excerpt-->"
```

Now you can have pages that show posts from one category while sorted by tags!

(I learned pieces of this solution online such as [this answer](https://stackoverflow.com/questions/28142299/jekyll-blog-show-posts-under-a-category) and [this answer](https://stackoverflow.com/questions/57199621/how-can-i-limit-the-number-of-lines-shown-on-the-homepage-of-a-jekyll-blog), and someone else's blog that I cannot find in my history anymore (the part about excerpts and readmore). So Let me know if you think that parts of my solution is from your post!)
